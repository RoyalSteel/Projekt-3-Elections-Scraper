Elections scraper
-
3.Projekt pro Engeto Python Akademii

Popis projektu
-
Cílem je extrahování výsledků parlamentních voleb v roce 2017 z jakéhokoli územního celeku z [tohoto odkazu](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ#11).
<br>Např. Prostějov ***Výběr
obce*** ***X*** [odkazuje sem](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103) z tohoto odkazu chceme vyscrapovat výsledky hlasování pro všechny obce, a jejich uložení do ***souboru .csv***.

Instalace knihoven
-
Knihovny použité v kódu jsou uložené v souboru ***requirements.txt.***

Pro jejich instalaci použijte příkaz:
<br>***pip install requirements.txt***

Spuštění projektu
-
Soubor ***election-scraper.py*** potřebuje ke své funkci dva argumenty:
<br>První argument obsahuje [odkaz](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103), který územní celek chcete scrapovat v tomto případě ( územní celek Prostějov ).
<br>Druhý argument obsahuje jméno výstupního souboru ( výsledky-prostějov-2017 )

Ukázka projektu
-
Výsledky pro okres Prostějov:
<br>1. argument "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
<br>2. argument 'výsledky-prostějov-2017'

Spuštění programu:
<br>election-scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" výsledky-prostějov-2017

Po ukončení programu:
<br>election-scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" výsledky-prostějov-2017
<br>Výsledky byly uloženy do souboru 'výsledky-prostějov-2017.csv'.
<br>
<br>Process finished with exit code 0

Výstup z programu Elections Scraper
-
Výstupem je soubor ***výsledky-prostějov-2017.csv*** který obsahuje data výsledků hlasování za územní celek Prostějov.

<br>Soubor ***výsledky-prostějov-2017.csv*** obsahuje tabulku která obsahuje sloupce s těmito parametry:
<br>1. kód obce
<br>2. název obce
<br>3. voliči v seznamu
<br>4. vydané obálky
<br>5. platné hlasy
<br>6. kandidující strany (co sloupec, to počet hlasů pro stranu pro všechny strany).

Závěrečné doporučení
-
Aby se dalo s výsledky ze souboru ***výsledky-prostějov-2017.csv*** dále pracovat doporučuji použít ***MS Excel*** nebo jiný tabulkový procesor který zvládá čtení a práci se soubory ***.csv***.
