"use strict";
(() => {
  const byId = id => document.getElementById(id);
  const statuses = {
    200: "OK — veiksmīgs pieprasījums; saņemts dokuments.",
    301: "Moved Permanently — resurss pārvietots; Location galvene.",
    403: "Forbidden — piekļuve liegta; pārtrauc pieprasījumus.",
    404: "Not Found — resurss nav atrasts.",
    429: "Too Many Requests — pārtrauc un ievēro servera norādes.",
    500: "Internal Server Error — servera kļūda."
  };
  const status = byId("l8-status");
  function updateStatus() {
    const value = status.value;
    byId("l8-status-out").textContent = value + " " + statuses[value] + "\n" +
      (Number(value) >= 400 ? "raise_for_status() → HTTPError" : "raise_for_status() → nav HTTPError");
  }
  status.addEventListener("change", updateStatus);
  updateStatus();

  const selector = byId("l8-selector");
  const source = byId("l8-selector-source").textContent;
  const parsed = new DOMParser().parseFromString(source, "text/html");
  function updateSelector() {
    const out = byId("l8-selector-out");
    try {
      const matches = [...parsed.body.querySelectorAll(selector.value)];
      out.textContent = "Atrasti: " + matches.length + "\n" +
        matches.map(node => node.outerHTML).join("\n");
    } catch {
      out.textContent = "Nederīgs CSS selektors. Izmēģini .price vai .product h2.";
    }
  }
  byId("l8-selector-run").addEventListener("click", updateSelector);
  selector.addEventListener("keydown", event => {
    if (event.key === "Enter") updateSelector();
  });
  updateSelector();

  const formats = {
    HTML: source,
    Python: 'products = [\n    {"name": "Python pamati", "price": 25.90},\n    {"name": "Datu analīze", "price": 32.50}\n]',
    JSON: JSON.stringify([{name:"Python pamati",price:25.9},{name:"Datu analīze",price:32.5}], null, 2),
    CSV: "name,price\nPython pamati,25.90\nDatu analīze,32.50"
  };
  const format = byId("l8-format");
  function updateFormat() { byId("l8-format-out").textContent = formats[format.value]; }
  format.addEventListener("change", updateFormat);
  updateFormat();
})();
