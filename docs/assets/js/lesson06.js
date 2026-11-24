"use strict";
(() => {
  const el = id => document.getElementById(id);
  const write = (id, text) => { el(id).textContent = text; };
  const pathUpdate = () => {
    const cwd = el("l6-cwd").value;
    const parts = ["kurss", ...(cwd === "root" ? [] : [cwd])];
    for (const part of el("l6-rel").value.split("/")) {
      if (part === "..") parts.pop();
      else parts.push(part);
    }
    const path = parts.join("/");
    write("l6-path-out", path + "\n" + (path === "kurss/datasets/pilsetas.txt" ? "Fails atrasts (modelī)." : "FileNotFoundError (modelī)."));
  };
  ["l6-cwd","l6-rel"].forEach(id => el(id).addEventListener("change", pathUpdate));
  pathUpdate();
  let file = "Rīga\nLiepāja\n";
  const showFile = () => write("l6-file", file || "(tukšs fails)");
  el("l6-file-run").addEventListener("click", () => {
    const mode = el("l6-mode").value;
    const line = el("l6-newline").value + "\n";
    if (mode === "r") write("l6-file-out", "Nolasīts:\n" + file);
    else {
      file = mode === "w" ? line : file + line;
      write("l6-file-out", mode === "w" ? "Iepriekšējais saturs pārrakstīts." : "Rinda pievienota.");
    }
    showFile();
  });
  el("l6-file-reset").addEventListener("click", () => { file = "Rīga\nLiepāja\n"; showFile(); write("l6-file-out", ""); });
  showFile();
  el("l6-filter-run").addEventListener("click", () => {
    const keyword = el("l6-keyword").value.toLowerCase();
    const text = el("l6-text").value;
    const rows = text ? text.replace(/\r\n/g, "\n").split("\n") : [];
    if (rows.at(-1) === "") rows.pop();
    const filtered = rows.filter(line => line.toLowerCase().includes(keyword));
    write("l6-filter-out", "Atlasītas rindas: " + filtered.length + "\n" + filtered.join("\n"));
  });
  const csvUpdate = () => {
    const delimiter = el("l6-delim").value;
    write("l6-csv-out", [["prece","daudzums","cena"],["Maize","2","1.50"],["Piens","3","1.20"]].map(row => row.join(delimiter)).join("\n") + "\n\ncsv.DictReader(file, delimiter=" + JSON.stringify(delimiter) + ")");
  };
  el("l6-delim").addEventListener("change", csvUpdate);
  csvUpdate();
})();
