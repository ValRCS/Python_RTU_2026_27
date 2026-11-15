"use strict";
(() => {
  // Fixed interactive models of Python collection operations; no Python code is evaluated.
  const el = id => document.getElementById(id);
  const repr = x => typeof x === "string" ? JSON.stringify(x) : String(x);
  const output = (id, message) => { if (el(id)) el(id).textContent = message; };

  // List explorer
  if (el("list-apply")) {
    const initial = ["ābols", "banāns", "bumbieris"];
    let items = [...initial];
    let last = "fruits = " + JSON.stringify(items);
    function renderList() {
      const visual = el("list-visual"); visual.replaceChildren();
      items.forEach((value, index) => {
        const cell = document.createElement("span"); cell.className = "lab-char";
        const strong = document.createElement("strong"); strong.textContent = value;
        const small = document.createElement("small"); small.textContent = index;
        cell.append(strong, small); visual.append(cell);
      });
      output("list-state", "fruits = " + JSON.stringify(items) + "\nlen(fruits) = " + items.length);
      output("list-python", last);
    }
    el("list-apply").addEventListener("click", () => {
      const action = el("list-action").value, value = el("list-value").value;
      const raw = el("list-index").value.trim(), index = Number(raw);
      const actual = index < 0 ? items.length + index : index;
      if (action === "append") {
        if (items.length >= 20) { last = "Demonstrācijas robeža: līdz 20 elementiem."; }
        else { items.push(value); last = "fruits.append(" + repr(value) + ")"; }
      } else if (action === "replace") {
        if (!raw || !Number.isSafeInteger(index)) last = "Indexam jābūt veselam skaitlim.";
        else if (actual < 0 || actual >= items.length) last = "IndexError: list assignment index out of range";
        else { items[actual] = value; last = "fruits[" + index + "] = " + repr(value); }
      } else if (action === "pop") {
        if (!items.length) last = "IndexError: pop from empty list";
        else { const removed = items.pop(); last = "fruits.pop()  # noņem " + repr(removed); }
      } else if (action === "remove") {
        const i = items.indexOf(value);
        if (i === -1) last = "ValueError: list.remove(x): x not in list";
        else { items.splice(i, 1); last = "fruits.remove(" + repr(value) + ")"; }
      }
      renderList();
    });
    el("list-reset").addEventListener("click", () => {
      items = [...initial]; last = "fruits = " + JSON.stringify(items); renderList();
    });
    el("list-action").addEventListener("change", () => {
      el("list-index-wrap").hidden = el("list-action").value !== "replace";
      el("list-value-wrap").hidden = el("list-action").value === "pop";
    });
    el("list-index-wrap").hidden = true;
    renderList();
  }

  // Text -> list -> text explorer
  if (el("text-source")) {
    function drawSplit() {
      const source = el("text-source").value, separator = el("split-mode").value;
      const words = separator === "whitespace"
        ? (source.trim() ? source.trim().split(/\s+/u) : [])
        : source.split(",");
      const original = [...words], raw = el("replace-index").value.trim();
      const index = Number(raw), valid = raw !== "" && Number.isSafeInteger(index);
      const actual = index < 0 ? words.length + index : index;
      const word = el("replace-word").value;
      let feedback = "";
      if (!valid) feedback = "Ievadi veselu aizstājamā elementa indeksu.";
      else if (actual < 0 || actual >= words.length) feedback = "IndexError: list assignment index out of range";
      else { words[actual] = word; feedback = "words[" + index + "] = " + repr(word); }
      const joiner = separator === "whitespace" ? " " : ",";
      output("text-result", "words = " + JSON.stringify(original) + "\n" +
        feedback + "\n" + (feedback.startsWith("words[") ? "new_text = " + repr(words.join(joiner)) : "Teksts nav mainīts.") +
        "\nSākotnējais text = " + repr(source));
    }
    ["text-source","split-mode","replace-index","replace-word"].forEach(id => {
      el(id).addEventListener(id === "split-mode" ? "change" : "input", drawSplit);
    }); drawSplit();
  }

  // Dictionary explorer: using Map avoids inherited object keys.
  if (el("dict-lookup")) {
    const initial = [["vārds", "Anna"], ["vecums", 28], ["pilsēta", "Rīga"]];
    let dictionary = new Map(initial);
    function renderDictionary(message) {
      const holder = el("dict-rows"); holder.replaceChildren();
      for (const [key, value] of dictionary) {
        const row = document.createElement("div"); row.className = "dict-row";
        const left = document.createElement("strong"); left.textContent = repr(key);
        const right = document.createElement("span"); right.textContent = repr(value);
        row.append(left, right); holder.append(row);
      }
      output("dict-state", message);
    }
    el("dict-lookup").addEventListener("click", () => {
      const key = el("dict-key").value;
      const has = dictionary.has(key);
      renderDictionary("student[" + repr(key) + "] → " +
        (has ? repr(dictionary.get(key)) : "KeyError: " + repr(key)) + "\n" +
        "student.get(" + repr(key) + ", \"nav norādīts\") → " +
        (has ? repr(dictionary.get(key)) : repr("nav norādīts")));
    });
    el("dict-update").addEventListener("click", () => {
      const key = el("dict-key").value, value = el("dict-value").value;
      if (!key) { renderDictionary("Atslēgai jābūt norādītai."); return; }
      if (dictionary.size >= 16 && !dictionary.has(key)) { renderDictionary("Demonstrācija ierobežota līdz 16 atslēgām."); return; }
      dictionary.set(key, value); // User-supplied value is a string from <input>.
      renderDictionary("student[" + repr(key) + "] = " + repr(value) + "\nIevadītās vērtības šajā laboratorijā ir str.");
    });
    el("dict-reset").addEventListener("click", () => {
      dictionary = new Map(initial); renderDictionary("Atjaunota sākotnējā vārdnīca.");
    });
    renderDictionary("Izvēlies atslēgu, lai meklētu vai atjauninātu tās vērtību.");
  }

  // Frequency counter, one word per step.
  if (el("freq-start")) {
    let tokens = [], position = 0, counts = new Map(), problem = "";
    function renderFrequency() {
      const holder = el("freq-words"); holder.replaceChildren();
      tokens.forEach((word, i) => {
        const chip = document.createElement("span");
        chip.className = "lab-token" + (i < position ? " is-done" : "");
        chip.textContent = word;
        holder.append(chip);
      });
      const asObject = Object.fromEntries(counts);
      output("freq-state", problem || ("Apstrādāti " + position + "/" + tokens.length + " vārdi.\ncounts = " +
        JSON.stringify(asObject) + (position === tokens.length ? "\nPabeigts." : "")));
      el("freq-next").disabled = Boolean(problem) || position >= tokens.length;
    }
    function resetFrequency() {
      const input = el("freq-text").value.trim().toLowerCase();
      tokens = input ? input.split(/\s+/u) : [];
      problem = tokens.length > 40 ? "Demonstrācija ierobežota līdz 40 vārdiem." : "";
      position = 0; counts = new Map();
      renderFrequency();
    }
    el("freq-start").addEventListener("click", resetFrequency);
    el("freq-next").addEventListener("click", () => {
      if (position >= tokens.length) return;
      const word = tokens[position];
      counts.set(word, (counts.get(word) || 0) + 1);
      position++; renderFrequency();
    });
    resetFrequency();
  }

  // Optional set explorer; sorted display does not imply set maintains order.
  if (el("set-source")) {
    function drawSet() {
      const input = el("set-source").value;
      const values = input.split(",").map(x => x.trim()).filter(x => x);
      const unique = [...new Set(values)].sort();
      output("set-result", "Saraksts: " + JSON.stringify(values) +
        "\nUnikālo elementu skaits: " + unique.length +
        "\nSakārtots attēlojums: " + JSON.stringify(unique) +
        "\nKopa pati nesaglabā garantētu izdrukas secību.");
    }
    el("set-source").addEventListener("input", drawSet); drawSet();
  }
})();
