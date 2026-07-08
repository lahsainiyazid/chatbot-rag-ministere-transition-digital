import json
import cloudscraper
from bs4 import BeautifulSoup 
docs=[]
urls=[("https://www.mmsp.gov.ma/fr/nos-services/portail-national-idarati","Portail National Idarati","Services aux citoyens"),
 ("https://www.mmsp.gov.ma/fr/nos-services/portail-national-des-r%C3%A9clamations-chikaya","Portail national des réclamations (Chikaya)","Services aux citoyens"),
 ("https://www.mmsp.gov.ma/fr/nos-services/portail-de-l%E2%80%99emploi-public","Portail de l’emploi public","Services aux citoyens"),
 ("https://www.mmsp.gov.ma/fr/nos-services/portail-de-transparence-et-acc%C3%A8s-%C3%A0-l%E2%80%99information-chafafiya","Portail de Transparence et accès à l’information (Chafafiya)","Services aux citoyens"),
  ("https://www.mmsp.gov.ma/fr/nos-services/centre-d%E2%80%99appel-et-d%E2%80%99orientation-administrative","Centre d’appel et d’orientation administrative","Services aux citoyens"),
 ("https://www.mmsp.gov.ma/fr/nos-services/portail-de-g%C3%A9olocalisation-des-services-publics","Portail de géolocalisation des Services Publics"," Services aux citoyens"),
 ("https://www.mmsp.gov.ma/fr/nos-services/bases-de-donn%C3%A9es-juridiques","Bases de données juridiques","Services aux fonctionnaires"),
 ("https://www.mmsp.gov.ma/fr/nos-services/simulateur-des-salaires","Simulateur des salaires","Services aux fonctionnaires"),
 ("https://www.mmsp.gov.ma/fr/nos-services/simulateur-des-pensions","Simulateur des pensions","Services aux fonctionnaires"),
 ("https://www.mmsp.gov.ma/fr/nos-services/portail-gouvernement-ouvert-ogp","Portail gouvernement ouvert OGP","Services aux fonctionnaires"),
 ("https://www.mmsp.gov.ma/fr/nos-services/r%C3%A9f%C3%A9rentiel-commun-de-la-grh","Référentiel Commun de la GRH","Services aux fonctionnaires"),
 ("https://www.mmsp.gov.ma/fr/nos-services/emtiaz","Emtiaz","Services aux fonctionnaires"),
 ("https://www.mmsp.gov.ma/fr/nos-services/site-du-fonds-de-modernisation-de-ladministration-publique-fomap","Site du Fonds de Modernisation de l'Administration Publique (FOMAP)","Services aux fonctionnaires"),
  ("https://www.mmsp.gov.ma/fr/nos-services/site-de-la-lutte-contre-la-corruption","Site de la lutte contre la corruption","Services aux fonctionnaires"),
 ("https://www.mmsp.gov.ma/fr/nos-services/conseil-sup%C3%A9rieur-de-la-fonction-publique","Conseil supérieur de la fonction publique","Services aux fonctionnaires"),
 ("https://www.mmsp.gov.ma/fr/nos-services/site-observatoire-genre-de-la-fonction-publique-ogfp","Site Observatoire genre de la Fonction publique (OGFP)","Services aux fonctionnaires"),
 ("https://www.mmsp.gov.ma/fr/nos-services/plateforme-d%E2%80%99%C3%A9change-du-r%C3%A9seau-du-droit-d%E2%80%99acc%C3%A8s-%C3%A0-l%E2%80%99information","Plateforme d’échange du Réseau du Droit d’accès à l’Information"," Services aux fonctionnaires"),
 ("https://www.mmsp.gov.ma/fr/nos-services/portail-de-capitalisation-du-programme-e-tamkeen","Portail de capitalisation du programme e-TAMKEEN","Services aux fonctionnaires")]
for url,titre,rubrique in urls:
    scraper=cloudscraper.create_scraper()
    response=scraper.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    boxes=soup.find_all("p")
    for box in boxes[:-2]:
        content=box.text.strip()
        if content:

            docs.append({"content":content,
                         "url":url,
                        "titre":titre,
                         "sous_rubrique":"",
                         "rubrique":rubrique,
                         "rubrique_principale":"Nos services "})
with open("full-services.json","w",encoding="utf-8") as f:
        json.dump(docs,f,ensure_ascii=False,indent=2)
