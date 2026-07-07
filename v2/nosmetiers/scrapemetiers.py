import json 
import cloudscraper 
from bs4 import BeautifulSoup 
scraper=cloudscraper.create_scraper()
urls_transition_numerique=[("https://www.mmsp.gov.ma/fr/nos-metiers/simplification-et-digitalisation-des-parcours-usagers","Simplification et digitalisation des parcours usagers","E-Gov","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/plateformes-technologiques-mutualis%C3%A9es","Plateformes technologiques mutualisées","E-Gov","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/gestion-des-relations-avec-les-usagers","Gestion des relations avec les usagers","E-Gov","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/l%E2%80%99offshoring-au-maroc","L'Offshoring au Maroc","Outsourcing & digital export","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/l%E2%80%99offre-offshoring-maroc","L'Offre Offshoring Maroc","Outsourcing & digital export","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/cadre-incitatif-informations-pratiques","Cadre incitatif : informations pratiques","Outsourcing & digital export","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/startups","Startups","Startups","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/accompagnement-%C3%A0-la-digitalisation-des-tpme","Accompagnement à la digitalisation des TPME","Digital entreprise","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/promotion-des-pme","Promotion des PME","Digital entreprise","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/cloud","Cloud","Cloud","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/connectivit%C3%A9","Connectivité","Connectivité","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/inclusion-num%C3%A9rique","Inclusion numérique","Inclusion numérique","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/formation-initiale","Formation initiale","Digital Talents","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/upskilling-et-reskilling","Upskilling et reskilling","Digital Talents","Transition Numérique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/promotion-de-loffre-num%C3%A9rique","Promotion de l'offre numérique","Digital Talents","Transition Numérique")]
"""
for url,titre,sous_rubrique,rubrique in urls_transition_numerique :
    response=scraper.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    boxes=soup.find_all("div",class_=["wg-inner-box","wg-collapsed-box-content"])
    for box in boxes:
        content=box.text.strip()
        if content:
            print(content)
"""            
urls_reforme_administration=[("https://www.mmsp.gov.ma/fr/node/4121","Charte des services publics","Réforme de L'Administration"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/organisation-de-l%E2%80%99administration","Organisation des administrations de l'État","Réforme de L'Administration"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/d%C3%A9concentration-administrative","Déconcentration administrative","Réforme de L'Administration"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/horaires-de-travail-et-jours-f%C3%A9ri%C3%A9s","Horaires de travail et jours fériés","Réforme de L'Administration"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/droit-d%E2%80%99acc%C3%A8s-%C3%A0-l%E2%80%99information","Droit d’accès à l’information","Réforme de L'Administration"),                           
 ("https://www.mmsp.gov.ma/fr/nos-metiers/%C3%A9thique-pr%C3%A9vention-et-lutte-contre-la-corruption","Éthique, prévention et lutte contre la corruption","Réforme de L'Administration"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/partenariat-pour-un-gouvernement-ouvert","Partenariat pour un Gouvernement Ouvert","Réforme de L'Administration"),  
 ("https://www.mmsp.gov.ma/fr/nos-metiers/appui-%C3%A0-l%E2%80%99innovation-publique","Appui à l’innovation publique","Réforme de L'Administration"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/institutions-de-contr%C3%B4le-et-d%E2%80%99inspection","Institutions de contrôle et d’inspection","Réforme de L'Administration"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/fonds-de-modernisation-de-l%E2%80%99administration","Fonds de modernisation (FOMAP)","Réforme de L'Administration")]
"""
for url ,titre, rubrique in urls_reforme_administration:
    response=scraper.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    boxes=soup.find_all("div",class_=["wg-inner-box","wg-collapsed-box-content"])
    for box in  boxes:
        content=box.text.strip()
        if content:
            print(content)
"""
urls_fonction_publique=[("https://www.mmsp.gov.ma/fr/nos-metiers/statut-g%C3%A9n%C3%A9ral-de-la-fonction-publique","Statut général de la fonction publique","Statut du fonctionnaire et Parcours Professionnel","Fonction publique ")]
for url,titre,sous_rubrique,rubrique in urls_fonction_publique:
    response=scraper.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    boxes=soup.find_all("div",class_=["wg-inner-box","wg-collapsed-box-content"])
    for box in boxes:
        content=box.text.strip()
        if content:
            print(content)

