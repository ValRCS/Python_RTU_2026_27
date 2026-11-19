# Python RTU GitHub Pages

Statiskā mācību vietne latviešu valodā. GitHub Settings → Pages → Deploy from a branch → main → /docs. Publicētā adrese: https://valrcs.github.io/Python_RTU_2026_27/

Atveriet `docs/index.html` lokāli vai izmantojiet `python -m http.server 8000 --directory docs` un http://localhost:8000. Nav vajadzīgs Node.js vai būvēšanas solis.

`docs/lessons/` satur tīmekļa lapas, savukārt repozitorija `lessons/` un `exercises/` paliek kanoniskie Python materiāli. Demonstrācijas ar JavaScript tikai modelē Python uzvedību; tās neizpilda Python kodu. Jaunu nodarbību veidojiet pēc esošo lapu struktūras, saglabājot relatīvos ceļus un saites uz oriģinālajiem materiāliem. Pārbaudiet mobilās ierīces, klaviatūras navigāciju, viktorīnas un kopēšanas pogas.

**4. nodarbība:** `lessons/04-collections/index.html` izmanto jau esošo `assets/js/exercises.js` viktorīnu pārbaudei un `assets/js/main.js` progresam, kopēšanai un navigācijai. Tikai kolekciju interaktīvie modeļi atrodas `assets/js/lesson04.js`; Python 3 demonstrāciju pirmkods ir `../lessons/04_collections/`.

**5. nodarbība:** `lessons/05-functions-modules/index.html` saglabā to pašu `main.js` un `exercises.js` sistēmu. `assets/js/lesson05.js` modelē parametru nodošanu, `print`/`return`, mainīgo tvērumu, moduļa izsaukumu un vienkāršu `assert` pārbaudi, **neizpildot lietotāja Python kodu**. Tīmekļa lapā ir 25 jautājumi, astoņu sadaļu progress, pieci uzdevumi ar atveramiem risinājumiem un saites uz atsevišķiem Python skriptiem.

**Git/VS Code papildu ceļvedis:** `resources/git-vscode.html` ir praktiska instrukcija par Git uzstādīšanu Windows un macOS, publiskā kursa repozitorija klonēšanu un atjaunināšanu VS Code. Lapa izmanto esošo `assets/js/main.js` (komandu kopēšana, progress) un `assets/js/exercises.js` (trīs pašpārbaudes jautājumi). GitHub konts, Git konfigurēšana un Push ir skaidri nošķirti kā neobligāta tēma. Saite atrodas sākumlapā, Resursu lapā un visu nodarbību galvenajā navigācijā.
