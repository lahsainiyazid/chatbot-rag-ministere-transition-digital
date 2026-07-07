import json 
import cloudscraper 
from bs4 import BeautifulSoup 
scraper=cloudscraper.create_scraper()
document=[]
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

for url,titre,sous_rubrique,rubrique in urls_transition_numerique :
    response=scraper.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    boxes=soup.find_all("div",class_=["wg-inner-box","wg-collapsed-box-content"])
    for box in boxes:
        content=box.text.strip()
        if content:
            document.append({"content":content,
                "url":url,
                              "titre":titre,
                              "sous_rubrique":sous_rubrique,
                              "rubrique":rubrique,
                              "rubrique_principale":"Nos métiers "})
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

for url ,titre, rubrique in urls_reforme_administration:
    response=scraper.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    boxes=soup.find_all("div",class_=["wg-inner-box","wg-collapsed-box-content"])
    for box in  boxes:
        content=box.text.strip()
        if content:
            document.append({"content":content,
                             "url":url,
                             "titre":titre,
                             "rubrique":rubrique,
                             "rubrique_principale":"Nos métiers"})
            

urls_fonction_publique=[("https://www.mmsp.gov.ma/fr/nos-metiers/statut-g%C3%A9n%C3%A9ral-de-la-fonction-publique","Statut général de la fonction publique","Statut du fonctionnaire et Parcours Professionnel","Fonction publique "),
                        ("https://www.mmsp.gov.ma/fr/nos-metiers/statuts-particuliers","Statuts particuliers","Statut du fonctionnaire et Parcours Professionnel","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/recrutement","Recrutement","Statut du fonctionnaire et Parcours Professionnel","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/syst%C3%A8me-de-r%C3%A9mun%C3%A9ration-et-indemnit%C3%A9","Système de rémunération et indemnité","Statut du fonctionnaire et Parcours Professionnel","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/notation-%C3%A9valuation","Notation & évaluation","Statut du fonctionnaire et Parcours Professionnel","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/promotion","Promotion","Statut du fonctionnaire et Parcours Professionnel","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/mobilit%C3%A9","Mobilité","Statut du fonctionnaire et Parcours Professionnel","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/cong%C3%A9s","Congés","Statut du fonctionnaire et Parcours Professionnel","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/r%C3%A9gime-disciplinaire","Régime disciplinaire","Statut du fonctionnaire et Parcours Professionnel","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/absence-non-justifi%C3%A9e","Absence non justifiée","Statut du fonctionnaire et Parcours Professionnel","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/retours-et-contentieux","Contrôle, contentieux et recours","Contrôle, contentieux et recours","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/commission-charg%C3%A9e-de-la-formation-continue","Formation continue","Formation","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/stages-de-formation","Stages de formation","Formation","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/rec-gpeec-outils-et-d%C3%A9marches","Gestion prévisionnelle des emplois et des compétences","Gestion prévisionnelle des emplois et des compétences","Fonction publique"),                        
 ("https://www.mmsp.gov.ma/fr/nos-metiers/hautes-fonctions-et-responsabilit%C3%A9s","Fonctions supérieures et postes de responsabilité","Fonctions supérieures et postes de responsabilité","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/observatoire-national-des-services-publics","Observatoire National des Services Publics","Observatoires","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-services/site-observatoire-genre-de-la-fonction-publique-ogfp","Observatoire National des Services Publics","Site Observatoire genre de la Fonction publique (OGFP)","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/effectifs-des-ressources-humaines-des-administrations-publiques","Statistiques des ressources humaines des administrations publiques","Observatoires","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/les-commissions-administratives-paritaires","Commissions administratives paritaires","Dialogue social/Instances consultatives","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/dialogue-social","Dialogue social/Instances consultatives","Dialogue social/Instances consultatives","Fonction publique"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/cadre-de-r%C3%A9f%C3%A9rence","Cadre de référence","Développement de l'utilisation de l’Amazighe","Développement de l'utilisation de l’Amazighe"),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/chantier-de-mise-en-%C5%93uvre-du-caract%C3%A8re-officiel-de-l%E2%80%99amazighe","Chantier de mise en œuvre de l’amazighe","Développement de l'utilisation de l’Amazighe","Développement de l'utilisation de l’Amazighe "),
 ("https://www.mmsp.gov.ma/fr/nos-metiers/m%C3%A9canismes-de-mise-en-%C5%93uvre","Mécanismes de mise en œuvre","Développement de l'utilisation de l’Amazighe ","Développement de l'utilisation de l’Amazighe ")]
for url,titre,sous_rubrique,rubrique in urls_fonction_publique:
    response=scraper.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    boxes=soup.find_all("div",class_=["wg-inner-box","wg-collapsed-box-content"])
    for box in boxes:
        content=box.text.strip()
        if content:
            document.append({"content":content,
                             "url":url,
                             "titre":titre,
                             "sous_rubrique":sous_rubrique,
                             "rubrique":rubrique,
                             "rubrique_principale":"Nos métiers"})



with open ("nos-metiers.json","w",encoding="utf-8") as f:            
    json.dump(document,f,ensure_ascii=False,indent=2)
