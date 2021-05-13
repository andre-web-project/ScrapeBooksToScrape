import requests
from bs4 import BeautifulSoup
import codecs
import re

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
        categories = category.strip()
        choixCategory.append(categories)
        link = a['href']
        linkV = link[2:]
        links[categories] = "https://books.toscrape.com/catalogue/category" + linkV


# fonction qui demande a utilisateur de choisir une ou toutes les catégorie
def demandeDeCategories():
    print(choixCategory)
    print("")
    choix = input("choisit ta categories parmit la listes si dessus : " )
    choixstr = str(choix)
    choixstr.lower()
    categorie = choixstr.capitalize()
    if categorie == "":
        print("Erreur !")
        print("Vous devez choisir une catégorie ou écrire Books pour tout sélectioner.")
        return demandeDeCategories()
    elif categorie in links:
        liens = links.get(categorie)
        if categorie == "Books":
            pass
        else:
            return liens, categorie
    else:
        print("Erreur !")
        print("Vous devez choisir une catégorie ou écrire Books pour tout sélectioner.")
        return demandeDeCategories()


retourFonction = demandeDeCategories()
newUrls = retourFonction[0]
retourCategorie = retourFonction[1]

response = requests.get(newUrls)

# fonction permettant de scrapper la totalité des livres d'une catégorie
if reponse.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    links = []
    liste = soup.findAll('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
    nomberBooks = soup.find('form', {'class': 'form-horizontal'}).find('strong').text
    if int(nomberBooks) > 20:
        pages = soup.find('li', {'class': 'next'}).find('a')
        pages2 = pages['href']
        pageNext = url[:-10]
        link = (pageNext + pages2)
        reponses = requests.get(link)
        soups = BeautifulSoup(reponses.text, 'lxml')
        liste2 = soups.findAll('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
        for li in liste2:
            a2 = li.find('a')
            x2 = a2["href"]
            x2 = re.sub('[..]', '', x2)
            y2 = x2[2:]
            link2 = y2[:-4]
            links.append('https://books.toscrape.com/catalogue' + link2 + '.html')
        for li in liste:
            a = li.find('a')
            x = a["href"]
            x = re.sub('[..]', '', x)
            y = x[2:]
            link = y[:-4]
            links.append('https://books.toscrape.com/catalogue' + link + '.html')
        print('il y a : ' + str(len(links)) + ' livres dans cette catégorie.')
    else:
        for li in liste:
            a = li.find('a')
            x = a["href"]
            x = re.sub('[..]', '', x)
            y = x[2:]
            link = y[:-4]
            links.append('https://books.toscrape.com/catalogue' + link + '.html')
        print('il y a : ' + str(len(links)) + ' livres dans cette catégorie.')


with codecs.open('scrappingBooks.csv', 'w', encoding='utf-8')as csvfile:
    col = retourCategorie
    csvfile.write(col)
    csvfile.write(links)



