import json
import cloudscraper
from bs4 import BeautifulSoup
document=[]
scraper=cloudscraper.create_scraper()
url_services_citoyens=[("https://www.mmsp.gov.ma/fr/nos-services/portail-national-idarati","Portail National Idarati"),
                       ("https://www.mmsp.gov.ma/fr/nos-services/portail-national-des-r%C3%A9clamations-chikaya","Portail national des réclamations (Chikaya)"),
("https://www.mmsp.gov.ma/fr/nos-services/portail-de-l%E2%80%99emploi-public","Portail de l’emploi public"),
 ("https://www.mmsp.gov.ma/fr/nos-services/portail-de-transparence-et-acc%C3%A8s-%C3%A0-l%E2%80%99information-chafafiya","Portail de Transparence et accès à l’information (Chafafiya)"),
 ("https://www.mmsp.gov.ma/fr/nos-services/centre-d%E2%80%99appel-et-d%E2%80%99orientation-administrative","Centre d’appel et d’orientation administrative"),
 ("https://www.mmsp.gov.ma/fr/nos-services/portail-de-g%C3%A9olocalisation-des-services-publics","Portail de géolocalisation des Services Publics")]
for url,titre in url_services_citoyens:
    response=scraper.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    boxes=soup.find_all("p")
    for box in boxes:
        content=box.text.strip()
        print(content)
