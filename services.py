import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document 
import json

def scrape_mmsp_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    content_div = soup.find("div", id="read_content")
    
    if content_div is None:
        return None
    
    for tag in content_div.find_all(["button", "script"]):
        tag.decompose()
    
    return content_div.get_text(separator="\n", strip=True)

url="https://www.mmsp.gov.ma/fr/nos-services/emtiaz"
print(scrape_mmsp_page(url))
urls_services= [ "https://www.mmsp.gov.ma/fr/nos-services/portail-du-sahara-marocain",
       "https://www.mmsp.gov.ma/fr/nos-services/portail-de-g%C3%A9olocalisation-des-services-publics",
       "https://www.mmsp.gov.ma/fr/nos-services/centre-d%E2%80%99appel-et-d%E2%80%99orientation-administrative",
       "https://www.mmsp.gov.ma/fr/nos-services/portail-de-transparence-et-acc%C3%A8s-%C3%A0-l%E2%80%99information-chafafiya",
       "https://www.mmsp.gov.ma/fr/nos-services/portail-de-l%E2%80%99emploi-public",
       "https://www.mmsp.gov.ma/fr/nos-services/portail-national-des-r%C3%A9clamations-chikaya",
       "https://www.mmsp.gov.ma/fr/nos-services/portail-national-idarati",
                "https://www.mmsp.gov.ma/fr/nos-services/portail-de-capitalisation-du-programme-e-tamkeen",
                "https://www.mmsp.gov.ma/fr/nos-services/plateforme-d%E2%80%99%C3%A9change-du-r%C3%A9seau-du-droit-d%E2%80%99acc%C3%A8s-%C3%A0-l%E2%80%99information",
                "https://www.mmsp.gov.ma/fr/nos-services/simulateur-des-pensions",
                "https://www.mmsp.gov.ma/fr/nos-services/site-observatoire-genre-de-la-fonction-publique-ogfp",
                "https://www.mmsp.gov.ma/fr/nos-services/conseil-sup%C3%A9rieur-de-la-fonction-publique",
                "https://www.mmsp.gov.ma/fr/nos-services/simulateur-des-salaires",
                "https://www.mmsp.gov.ma/fr/nos-services/portail-gouvernement-ouvert-ogp",
                "https://www.mmsp.gov.ma/fr/nos-services/r%C3%A9f%C3%A9rentiel-commun-de-la-grh",
                "https://www.mmsp.gov.ma/fr/nos-services/site-du-fonds-de-modernisation-de-ladministration-publique-fomap",
                "https://www.mmsp.gov.ma/fr/nos-services/site-de-la-lutte-contre-la-corruption",
                "https://www.mmsp.gov.ma/fr/nos-services/emtiaz",
                "https://www.mmsp.gov.ma/fr/nos-services/bases-de-donn%C3%A9es-juridiques"]
documents=[]
for url in urls_services:
    try:
      text=scrape_mmsp_page(url)
      if text:
          doc=Document(page_content=text,
                     metadata={"url":url,"rubrique":"nos-services"})
          documents.append(doc)
    except Exception as e:
        print(f"Error {e} on url {url} ")

dataset=[]
for doc in documents:
    dataset.append({"content":doc.page_content,
                    "metadata":doc.metadata})
    with open ("services.json","w",encoding="utf-8") as f:
        json.dump(dataset,f,ensure_ascii=False,indent=2)






