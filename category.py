import requests
from bs4 import BeautifulSoup
import codecs
import re

url ="https://books.toscrape.com/catalogue/category/books_1/index.html"
reponse = requests.get(url)

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

def demandeDeCategories():
    print(choixCategory)
    print("")
    print(input("choisit ta categories parmit la listes si dessus : " ))

demandeDeCategories()
'''
if reponse.ok:
    soup = BeautifulSoup(reponse.text, 'lxml')
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
'''


