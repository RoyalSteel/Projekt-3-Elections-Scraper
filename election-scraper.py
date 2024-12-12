"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Petr Král
email: petr.kral36@seznam.cz
"""

import requests
import sys
from bs4 import BeautifulSoup
import csv
import validators

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def scrape_village_results(village_url):
    html = fetch_page(village_url)
    soup = BeautifulSoup(html, 'html.parser')

    village_code = soup.find('h3').text.split()[0].strip()
    titles = soup.find_all('h3', class_="")
    village_name = next((title.text.split()[1] for title in titles if "Obec" in title.text), "")

    tables = soup.find_all('table')
    voters_info_table = tables[0]
    voters_info_rows = voters_info_table.find_all('tr')
    voters_in_list = voters_info_rows[2].find_all('td')[3].text.strip()
    issued_envelopes = voters_info_rows[2].find_all('td')[4].text.strip()
    valid_votes = voters_info_rows[2].find_all('td')[7].text.strip()
    party_results = {}

    rows = []
    for table in tables[1:]:
        table_rows = table.find_all("tr")[2:]
        rows.extend(table_rows) 

    for row in rows:
        name_cell = row.find("td", class_="overflow_name")
        total_cells = row.find_all("td", class_="cislo")
        if name_cell and len(total_cells) > 1:
            total_cell = row.find_all("td", class_="cislo")[1]
            if name_cell and total_cell:
                name = name_cell.text.strip()
                total = total_cell.text.strip()
                party_results[name] = total

    return {
        'village_code': village_url.split("&xobec=")[1].split("&xvyber=")[0],
        'village_name': village_name,
        'voters_in_list': voters_in_list,
        'issued_envelopes': issued_envelopes,
        'valid_votes': valid_votes,
        'party_results': party_results
    }

def main():
    if len(sys.argv) < 3:
        print('Pro správné spuštění programu je nutné zadat nejprve odkaz "http://..." a následně cestu k souboru, kam se mají data uložit.')
        return
    
    url = sys.argv[1]
    file_name = sys.argv[2]

    if validators.url(url) is not True:
        print("URL adresa není ve správném formátu")

    html = fetch_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    cislo_cells = soup.find_all("td", class_="cislo")
    urls = []

    for cell in cislo_cells:
        link = cell.find("a")
        if link:
            href = link.get("href")
            base_url = url.split("/ps32?")[0]
            new_url = f"{base_url}/{href}" 
            urls.append(new_url)

    all_results = []
    all_parties = set()
    for url in urls:
        village_results = scrape_village_results(url)
        all_results.append(village_results)
        all_parties.update(village_results['party_results'].keys())

    all_parties = sorted(all_parties)

    with open(f"{file_name}.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        header = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy'] + list(all_parties)
        writer.writerow(header)

        for village in all_results:
            row = [
                village['village_code'],
                village['village_name'],
                village['voters_in_list'],
                village['issued_envelopes'],
                village['valid_votes']
            ]
            for party in all_parties:
                row.append(village['party_results'].get(party, '0'))
            writer.writerow(row)

    print(f"Výsledky byly uloženy do souboru '{file_name}.csv'.")

if __name__ == '__main__':
    main()
