"use strict";
(() => {
  const el = id => document.getElementById(id);
  const write = (id, text) => { el(id).textContent = text; };
  const pyType = value => value === null ? "NoneType" : Array.isArray(value) ? "list" : typeof value === "object" ? "dict" : typeof value === "boolean" ? "bool" : typeof value === "string" ? "str" : Number.isInteger(value) ? "int (aptuvens modelis)" : "float";
  const validate = () => {
    try {
      const parsed = JSON.parse(el("l7-json-input").value);
      write("l7-json-out", "Derīgs JSON. Aptuvenais Python tips: " + pyType(parsed) + "\n" + JSON.stringify(parsed, null, 2));
    } catch {
      write("l7-json-out", "Nederīgs JSON. Pārbaudi pēdiņas, komatus, iekavas un true/false/null.");
    }
  };
  el("l7-json-input").addEventListener("input", validate);
  const example = (id, value) => el(id).addEventListener("click", () => { el("l7-json-input").value = value; validate(); });
  example("l7-json-good", '{"pilsēta": "Rīga", "aktīvs": true}');
  example("l7-json-bad", "{'pilsēta': 'Rīga', 'aktīvs': True}");
  example("l7-json-comma", '{"pilsēta": "Rīga",}');
  validate();
  const env = () => write("l7-env-out", el("l7-install").value === el("l7-run-env").value ? "Importēšana izdodas (modelī, ja instalācija veiksmīga)." : "ModuleNotFoundError (modelī — pakotne nav instalēta izvēlētajā vidē).");
  ["l7-install","l7-run-env"].forEach(id => el(id).addEventListener("change", env));
  env();
  let x;
  const kernel = () => write("l7-kernel", x === undefined ? "Kodols: x nav definēts." : "Kodols: x = " + x);
  el("l7-cell1").addEventListener("click", () => {
    const raw = el("l7-x").value.trim();
    if (!raw || !Number.isSafeInteger(Number(raw)) || Math.abs(Number(raw)) > Number.MAX_SAFE_INTEGER / 2) {
      write("l7-cell-out", "Modelī ievadi drošu veselu skaitli.");
      return;
    }
    x = Number(raw); kernel();
  });
  el("l7-cell2").addEventListener("click", () => write("l7-cell-out", x === undefined ? "NameError: name 'x' is not defined" : String(x * 2)));
  el("l7-reset").addEventListener("click", () => { x = undefined; kernel(); write("l7-cell-out", ""); });
  kernel();
})();
