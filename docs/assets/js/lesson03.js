"use strict";
(() => {
  // This script models small, fixed Python examples; it does not evaluate Python code.
  const get = id => document.getElementById(id);
  const rStart = get("range-start"), rStop = get("range-stop"), rStep = get("range-step");
  const track = get("range-track"), rangeState = get("range-state");
  let numbers = [], position = 0, error = "";
  function drawRange() {
    track.replaceChildren();
    for (let i = 0; i < numbers.length; i++) {
      const chip = document.createElement("span");
      chip.className = "lab-token" + (i < position ? " is-done" : "");
      chip.textContent = String(numbers[i]);
      track.append(chip);
    }
    if (error) {
      rangeState.textContent = error;
    } else if (!numbers.length) {
      rangeState.textContent = "Tukša secība: nav nevienas iterācijas.";
    } else {
      const total = numbers.slice(0, position).reduce((sum, n) => sum + n, 0);
      rangeState.textContent = "Izpildītas " + position + "/" + numbers.length + " iterācijas. " +
        (position ? "Pēdējais n = " + numbers[position - 1] + ". " : "") +
        "total = " + total + (position === numbers.length ? ". Cikls pabeigts." : ".");
    }
    get("range-next").disabled = Boolean(error) || position === numbers.length;
  }
  function resetRange() {
    position = 0; numbers = []; error = "";
    const controls = [rStart, rStop, rStep];
    const values = controls.map(el => Number(el.value));
    const [start, stop, step] = values;
    if (controls.some(el => !el.value.trim() || !Number.isSafeInteger(Number(el.value)))) {
      error = "Ievadi veselus skaitļus.";
    } else if (step === 0) {
      error = "ValueError: range() arg 3 must not be zero";
    } else {
      for (let n = start; step > 0 ? n < stop : n > stop; n += step) {
        if (numbers.length >= 40 || !Number.isSafeInteger(n)) {
          error = "Demonstrācija ierobežota līdz 40 drošām iterācijām.";
          break;
        }
        numbers.push(n);
      }
    }
    get("range-code").textContent = "total = 0\nfor n in range(" + start + ", " + stop + ", " + step + "):\n    total += n";
    drawRange();
  }
  if (rStart && rStop && rStep) {
    [rStart, rStop, rStep].forEach(el => el.addEventListener("input", resetRange));
    get("range-next").addEventListener("click", () => { position++; drawRange(); });
    get("range-reset").addEventListener("click", resetRange);
    resetRange();
  }

  let whileCount = 0, whileDone = false;
  function drawWhile() {
    const state = get("while-state");
    state.textContent = whileDone ? "i = 4; nosacījums 4 < 4 ir False. Izvada “Pabeigts”." :
      "i = " + whileCount + "; " +
      (whileCount < 4
        ? "nosacījums ir True. Nākamajā solī izdrukā " + whileCount + " un palielina i."
        : "nosacījums ir False. Nākamajā solī iziet no cikla.");
    get("while-next").disabled = whileDone;
  }
  if (get("while-next") && get("while-reset")) {
    get("while-next").addEventListener("click", () => { if (whileCount < 4) whileCount++; else whileDone = true; drawWhile(); });
    get("while-reset").addEventListener("click", () => { whileCount = 0; whileDone = false; drawWhile(); });
    drawWhile();
  }

  const stringText = get("string-value"), stringIndex = get("string-index");
  const stringFrom = get("string-from"), stringTo = get("string-to");
  function drawString() {
    const chars = Array.from(stringText.value); // Unicode code points, as in Python str indexing.
    const fields = [stringIndex, stringFrom, stringTo];
    const valid = fields.every(el => el.value.trim() !== "" && Number.isSafeInteger(Number(el.value)));
    const index = Number(stringIndex.value), start = Number(stringFrom.value), stop = Number(stringTo.value);
    const actual = index < 0 ? chars.length + index : index;
    const inBounds = valid && actual >= 0 && actual < chars.length;
    const container = get("string-chars"); container.replaceChildren();
    chars.forEach((char, i) => {
      const cell = document.createElement("span");
      cell.className = "lab-char" + (inBounds && actual === i ? " is-selected" : "");
      const label = document.createElement("strong");
      label.textContent = char === " " ? "␠" : char;
      const number = document.createElement("small"); number.textContent = String(i);
      cell.append(label, number); container.append(cell);
    });
    const selected = valid ? (inBounds ? JSON.stringify(chars[actual]) : "IndexError: string index out of range") : "Ievadi veselus skaitļus.";
    const slice = valid ? JSON.stringify(chars.slice(start, stop).join("")) : "—";
    get("string-result").textContent =
      "len(text) = " + chars.length + "\n" +
      "text[" + stringIndex.value + "] → " + selected + "\n" +
      "text[" + stringFrom.value + ":" + stringTo.value + "] → " + slice;
  }
  if (stringText && stringIndex && stringFrom && stringTo) {
    [stringText, stringIndex, stringFrom, stringTo].forEach(el => el.addEventListener("input", drawString));
    drawString();
  }

  function drawMethod() {
    const input = get("method-text"), op = get("method-op"), output = get("method-result");
    const text = input.value; let method = "", value;
    switch (op.value) {
      case "strip": method = ".strip()"; value = text.trim(); break;
      case "lower": method = ".lower()"; value = text.toLowerCase(); break;
      case "upper": method = ".upper()"; value = text.toUpperCase(); break;
      case "replace": method = '.replace("a", "@")'; value = text.split("a").join("@"); break;
      case "count": method = '.count("a")'; value = Array.from(text).filter(c => c === "a").length; break;
      case "startswith": method = '.startswith("R")'; value = text.startsWith("R"); break;
      case "endswith": method = '.endswith("a")'; value = text.endsWith("a"); break;
      default: return;
    }
    const rendered = typeof value === "string" ? JSON.stringify(value) : value === true ? "True" : value === false ? "False" : String(value);
    output.textContent = "text = " + JSON.stringify(text) + "\ntext" + method + " → " + rendered + "\nSākotnējais text nemainās.";
  }
  if (get("method-text") && get("method-op")) {
    get("method-text").addEventListener("input", drawMethod);
    get("method-op").addEventListener("change", drawMethod);
    drawMethod();
  }
})();