import requests
from bs4 import BeautifulSoup
import codecs
import os
from category import scrappingSelectionDemander
import urllib.request as ulib


# creation fonction recherchant les details du livre demandé
def rechercheInfosBook():
    links = scrappingSelectionDemander()
    valeurs = []
    for url in links:
        urls = url
        reponse = requests.get(urls)
        if reponse.ok:
            soup = BeautifulSoup(reponse.text, "lxml")
            tds = soup.findAll('td')
            title = soup.find("h1").text
            price_including_taxs = tds[3].text
            price_including_tax = price_including_taxs[1:]
            price_excluding_taxs = tds[2].text
            price_excluding_tax = price_excluding_taxs[1:]
            number_available = tds[5].text
            product_description = tds[1].text
            category = soup.findAll('a')[3].text
            review_rating = soup.find('p', class_='star-rating')['class'][1].lower()
            liens = soup.find('img')['src']
            liensImage = "https://books.toscrape.com/" + liens[6:]
            image_url = liensImage
            valeur = [title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url]
            valeurs.append(valeur)
    print("")
    print("Les données des livres de la selection ont etait récuperer ainsi que les images de couvertures.")
    return valeurs


# creation fonction de requette de url des images
def get_html(source):
    with ulib.urlopen(source) as u:
        return u.read()


def impressionDuDetails():
    valeurs = rechercheInfosBook()
    images = []
    tout = valeurs[1]
    categ = tout[5]
    for i in valeurs:
        image = i[-1]
        images.append(image)
    entre = input('Voulez creer un fichier avec ces données et enregistrer les images ? ')
    validation = entre.lower()
    entetes = [
        u'Title',
        u'price including tax',
        u'price excluding tax',
        u'number available',
        u'product description',
        u'category',
        u'review rating',
        u'image url'
    ]
    ligneEntete = ';'.join(entetes) + '\n'
    # creation du dossier pour accueillir les images
    if validation == "oui":
        print("Le fichier csv a était généré.")
        print("")
        if not os.path.exists("imagesCouv" + categ):
            os.makedirs("imagesCouv" + categ)
        for i, img in enumerate(images):
            nom = img.split("/")[-1]
            dest = os.path.join("imagesCouv"+ categ, nom)
            if os.path.exists(dest):
                continue
            try:
                contenu = get_html(img)
            except Exception as e:
                continue
            with open(dest, "wb") as f:
                f.write(contenu)
        print("Les images ont etait enregistrées .")
        with codecs.open('scrappingBooks' + categ + '.csv', 'w', encoding='utf-8') as file:
            file.write(ligneEntete)
            for row in valeurs:
                ligne = ';'.join(row) + '\n'
                file.write(ligne)
    else:
        print("Fin de la recherche.")
        print("")


impressionDuDetails()