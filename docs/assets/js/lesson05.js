"use strict";

// 5. nodarbības pārskatāmās laboratorijas. Tie ir konkrētu Python piemēru
// modeļi JavaScript, NEVIS Python koda izpilde pārlūkā.
(() => {
  const el = id => document.getElementById(id);
  const write = (id, message) => {
    const target = el(id);
    if (target) target.textContent = message;
  };
  const numeric = id => {
    const raw = el(id).value.trim();
    if (!raw) return null;
    const value = Number(raw);
    return Number.isFinite(value) ? value : null;
  };
  const literal = value => JSON.stringify(value);
  const countWords = text => {
    const words = text.toLowerCase().trim();
    const counts = new Map();
    if (!words) return counts;
    for (const word of words.split(/\s+/u)) {
      counts.set(word, (counts.get(word) || 0) + 1);
    }
    return counts;
  };
  const dictDisplay = counts => "{"
    + [...counts].map(([key, value]) => literal(key) + ": " + value).join(", ")
    + "}";

  // 1. Izsaukums ar diviem skaitliskiem argumentiem.
  if (el("fn-run")) {
    const run = () => {
      const a = numeric("fn-a");
      const b = numeric("fn-b");
      if (a === null || b === null) {
        write("fn-result", "Ievadi divus galīgus skaitļus. Tukšs lauks nav skaitlis.");
        return;
      }
      write("fn-result",
        "add(" + a + ", " + b + ")\n"
        + "Funkcijas lokālie parametri: a = " + a + ", b = " + b
        + "\nreturn a + b  →  " + (a + b));
    };
    el("fn-run").addEventListener("click", run);
    run();
  }

  // 2. print izdrukā, return atgriež vērtību.
  if (el("return-run")) {
    const run = () => {
      const number = numeric("return-number");
      if (number === null) {
        write("return-output", "Ievadi skaitli.");
        return;
      }
      const printed = number * 2;
      const variant = el("return-variant").value;
      if (variant === "print") {
        write("return-output",
          "double_a(" + number + ")\n"
          + "Ekrānā (stdout): " + printed + "\n"
          + "Mainīgajā pēc izsaukuma: None\n"
          + "print() pati atgriež None; funkcijā nav return.");
      } else {
        write("return-output",
          "double_b(" + number + ")\n"
          + "Ekrānā (stdout): nekas\n"
          + "Mainīgajā pēc izsaukuma: " + printed + "\n"
          + "return nodod vērtību funkcijas izsaucējam.");
      }
    };
    el("return-run").addEventListener("click", run);
    el("return-variant").addEventListener("change", run);
    run();
  }

  // 3. Lokālā un ārējā mainīgā piesaiste nav viens un tas pats.
  if (el("scope-run")) {
    const run = () => {
      const outside = el("scope-outer").value;
      const inside = el("scope-local").value;
      if (!outside.trim() || !inside.trim()) {
        write("scope-output", "Norādi abas pilsētas.");
        return;
      }
      write("scope-output",
        "Ārējais city = " + literal(outside) + "\n"
        + "show_city() atgriež: " + literal(inside) + "\n"
        + "Pēc izsaukuma ārējais city joprojām ir: " + literal(outside));
    };
    el("scope-run").addEventListener("click", run);
    run();
  }

  // 4. Paša moduļa funkcijas izsaukuma modelis.
  if (el("module-run")) {
    const run = () => {
      const source = el("module-text").value;
      if (source.length > 180) {
        write("module-output", "Demonstrācijai izmanto ne vairāk kā 180 rakstzīmes.");
        return;
      }
      const counts = countWords(source);
      write("module-output",
        "word_tools.count_words(" + literal(source) + ")\n"
        + "→ " + dictDisplay(counts) + "\n"
        + "Dažādo vārdu skaits: " + counts.size);
    };
    el("module-run").addEventListener("click", run);
    run();
  }

  // 5. Vienas prognozes pārbaude, piemērojot fiksētu count_words loģiku.
  if (el("test-run")) {
    const run = () => {
      const raw = el("test-expected").value.trim();
      const expected = Number(raw);
      const source = el("test-text").value;
      if (!raw || !Number.isSafeInteger(expected) || expected < 0) {
        write("test-result", "Sagaidāmais skaits ir nenegatīvs vesels skaitlis.");
        return;
      }
      if (source.length > 180) {
        write("test-result", "Demonstrācijas robeža: ne vairāk kā 180 rakstzīmes.");
        return;
      }
      const actual = countWords(source).get("rīga") || 0;
      const ok = actual === expected;
      write("test-result",
        "assert count_words(" + literal(source) + ').get("rīga", 0) == ' + expected
        + "\nFaktiskais skaits: " + actual
        + "\nSagaidāmais skaits: " + expected
        + "\n" + (ok ? "PASS — nosacījums ir patiess." : "FAIL — AssertionError: skaiti atšķiras."));
      el("test-result").classList.toggle("good", ok);
      el("test-result").classList.toggle("bad", !ok);
    };
    el("test-run").addEventListener("click", run);
    run();
  }
})();
