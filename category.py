import requests
from bs4 import BeautifulSoup
import codecs
import re

# creation de url de base avec ca requette sur la page home du site
url ="https://books.toscrape.com/catalogue/category/books_1/index.html"
reponse = requests.get(url)


# scrapping de chaque categories ainsi que toutes leurs pages
if reponse.ok:
    soup = BeautifulSoup(reponse.text, 'lxml')
    links = {}
    choixCategory = []
    liste = soup.find('ul', {'class': 'nav nav-list'})
    listes = liste.findAll('li')
    for li in listes:
        a = li.find('a')
        category = a.text
        category = re.sub('[\n]', '', category)
        categorySansEspace = category.strip()
        categoriesSansMajuscule = categorySansEspace.upper()
        categorySansEspace = categoriesSansMajuscule.capitalize()
        choixCategory.append(categorySansEspace)
        link = a['href']
        linkV = link[2:]
        links[categorySansEspace] = "https://books.toscrape.com/catalogue/category" + linkV

# suppression de la categorie Books qui n'en est pas une
# del choixCategory[0]

# fonction qui demande a utilisateur de choisir une ou toutes les catégorie
def demandeDeCategories():
    print(choixCategory)
    print("")
    choix = input("choisis ta categories parmit la listes si dessus ou Books pour tout selectionner : " )
    choixstr = str(choix)
    choixstr.lower()
    categorie = choixstr.capitalize()
    if categorie == "":
        print("Erreur !")
        print("Vous devez choisir une catégorie ou écrire Books pour tout sélectionner.")
        return demandeDeCategories()
    elif categorie in links:
        liens = links.get(categorie)
        return liens, categorie
    else:
        print("Erreur !")
        print("Vous devez choisir une catégorie ou écrire Books pour tout sélectionner.")
        return demandeDeCategories()


# variable de recuperation de valeurs necessaires pour les autres fonction
retourFonction = demandeDeCategories()
newUrls = retourFonction[0]
retourCategorie = retourFonction[1]
response = requests.get(newUrls)


# fonction permettant de scrapper la totalité des livres d'une catégorie
if reponse.ok:
    links = []
# rajout de la fonction Books pour recuperer la totalité de livres----------
    if retourCategorie == 'Books':
        soup = BeautifulSoup(reponse.text, "lxml")
        page = soup.find('li', {'class': 'next'}).find('a')
        nombrePage = soup.find('li', {'class': 'current'}).text
        pageSansEspace = nombrePage.strip()
        totalPage = pageSansEspace[10:]
        pageTotal = int(totalPage) - 1
        urlPageNext = page['href']
        books = []
        newUrl = "https://books.toscrape.com/catalogue/category/books_1/" + urlPageNext
        books.append(newUrls)
        books.append(newUrl)
        for i in range(pageTotal):
            newUrl = "https://books.toscrape.com/catalogue/category/books_1/" + urlPageNext
            newResponse = requests.get(newUrl)
            soups = BeautifulSoup(newResponse.text, "lxml")
            pages = soups.find('li', {'class': 'next'}).find('a')
            urlPageNext = pages['href']
            newUrl = "https://books.toscrape.com/catalogue/category/books_1/" + urlPageNext
            books.append(newUrl)
        for l in books:
            r = requests.get(l)
            s = BeautifulSoup(r.text, "lxml")
            liste = s.findAll('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
            for li in liste:
                a2 = li.find('a')
                x2 = a2["href"]
                x2 = re.sub('[..]', '', x2)
                y2 = x2[2:]
                link2 = y2[:-4]
                links.append('https://books.toscrape.com/catalogue' + link2 + '.html')
        print('il y a : ' + str(len(links)) + ' livres dans cette catégorie.')
        print('Un fichier csv avec ces données à etait générer')
# fin du rajout de code ---------------------------------------------------------------
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        liste = soup.findAll('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
        nomberBooks = soup.find('form', {'class': 'form-horizontal'}).find('strong').text
        if int(nomberBooks) > 20:
            pages = soup.find('li', {'class': 'next'}).find('a')
            pages2 = pages['href']
            pageNext = url[:-10]
            liens = (pageNext + pages2)
            reponses = requests.get(liens)
            soups = BeautifulSoup(reponses.text, 'lxml')
            liste2 = soups.findAll('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
        # rajout du code pageNext -------------------------------------------
            page = soup.find('li', {'class': 'next'}).find('a')
            nombrePage = soup.find('li', {'class': 'current'}).text
            pageSansEspace = nombrePage.strip()
            totalPage = pageSansEspace[10:]
            pageTotal = int(totalPage) -2
            urlPageNext = page['href']
            newUrl2 = newUrls[:-10]
            link = []
            link.append(newUrls)
            link.append(newUrl2 + urlPageNext)
            for i in range(pageTotal):
                newUrl = newUrl2 + urlPageNext
                newResponse = requests.get(newUrl)
                soups = BeautifulSoup(newResponse.text, "lxml")
                pages = soups.find('li', {'class': 'next'}).find('a')
                urlPageNext = pages['href']
                newUrl = newUrl2 + urlPageNext
                link.append(newUrl)
            for l in link:
                r = requests.get(l)
                s = BeautifulSoup(r.text, "lxml")
                liste1 = s.findAll('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
                for li in liste1:
                    a2 = li.find('a')
                    x2 = a2["href"]
                    x2 = re.sub('[..]', '', x2)
                    y2 = x2[2:]
                    link2 = y2[:-4]
                    links.append('https://books.toscrape.com/catalogue' + link2 + '.html')
            # fin du code rajouter ---------------------------------------------------------
            print('il y a : ' + str(len(links)) + ' livres dans cette catégorie.')
            print('Un fichier csv avec ces données à etait générer')
        else:
            for li in liste:
                a = li.find('a')
                x = a["href"]
                x = re.sub('[..]', '', x)
                y = x[2:]
                link = y[:-4]
                links.append('https://books.toscrape.com/catalogue' + link + '.html')
            print('il y a : ' + str(len(links)) + ' livres dans cette catégorie.')
            print('Un fichier csv avec ces données à etait générer')


# ligne necessaires pour la mise en page du fichier csv
entetes = [
    u'categorie',
    u'liens du livre'
]
ligneEntete = ';'.join(entetes) + '\n'


# code pour l'extraction du fichier csv de la categorie demander
with codecs.open('scrappingCategories' + retourCategorie + '.csv', 'w', encoding='utf-8') as file:
    file.write(ligneEntete)
    for row in links:
        ligne = retourCategorie+ ';' + row + '\n'
        file.write(ligne)
