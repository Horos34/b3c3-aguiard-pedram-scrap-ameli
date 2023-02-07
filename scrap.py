from bs4 import BeautifulSoup
import requests

url = "http://annuairesante.ameli.fr/recherche.html"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
payload = {
    "type": "ps",
    "ps_profession": "34",
    "ps_profession_label" : "Médecin généraliste",
    "ps_sexe": "2",
    "ps_localisation" : "HERAULT (34)",
    "localisation_category": "departements",
    "submit_final": "Rechercher"
}

req = requests.Session()
page = req.post(url,payload,header)

if page.status_code == 200:
    linkSearch = page.url

soup = BeautifulSoup(page.text, "html.parser")

num_tel = soup.find_all("div", {"class": "item left tel"})

list_num = []

for num in num_tel:
    res = num.decode_contents().replace("\xa0", " ")
    list_num.append(res)

print(list_num)