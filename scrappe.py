import requests
from bs4 import BeautifulSoup
import re
from enregistrementPic import enregistrement_des_images
from extractionCsv import impression_du_details


# fonction de recherche des elements demander pour chaque livres
def recherche_infos_book(links):
    valeurs = []
    for url in links:
        urls = url
        reponse = requests.get(urls)
        if reponse.ok:
            soup = BeautifulSoup(reponse.text, "html.parser")
            tds = soup.findAll('td')
            ps = soup.findAll("p")
            title = soup.find("h1").text
            price_including_taxs = tds[3].text
            price_including_tax = price_including_taxs[1:]
            price_excluding_taxs = tds[2].text
            price_excluding_tax = price_excluding_taxs[1:]
            number_available = tds[5].text
            product_description = ps[3].text
            product_description = product_description.replace(";", ",")
            category = soup.findAll('a')[3].text
            review_rating = soup.find('p', class_='star-rating')['class'][1].lower()
            liens = soup.find('img')['src']
            liensImage = "https://books.toscrape.com/" + liens[6:]
            image_url = liensImage
            valeur = [title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url]
            valeurs.append(valeur)
    return valeurs


# fonction de scrapping des noms et liens de chaque categories
def scrappe_categorie():
    # creation de url de base avec ca requette sur la page home du site
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    reponse = requests.get(url)
    # scrapping de chaque categories ainsi que toutes leurs pages
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, "html.parser")
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
    return links, choixCategory


# fonction menu de selection de category
def selection_category(links, choixCategory):
    print("")
    print(choixCategory)
    print("")
    choix = input("choisis ta categories parmit la listes si dessus ou Books pour tout selectionner : " )
    choixstr = str(choix)
    choixstr.lower()
    categorie = choixstr.capitalize()
    if categorie == "":
        print("Erreur !")
        print("Vous devez choisir une catégorie ou écrire Books pour tout sélectionner.")
        return selection_category(links, choixCategory)
    elif categorie in links:
        liens = links.get(categorie)
        return liens, categorie
    else:
        print("Erreur !")
        print("Vous devez choisir une catégorie ou écrire Books pour tout sélectionner.")
        return selection_category(links, choixCategory)


# fonction de scrapping de livre de la selection demander gere aussi le pagging
def recherche_categorie(liens, cat):
    # url de base
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    # variable de recuperation des valeurs necessaires pour la suite du code
    reponse = requests.get(url)
    newurls = liens
    retourcategorie = cat
    response = requests.get(newurls)
    if reponse.ok:
        links = []
    # rajout de la fonction Books pour recuperer la totalité de livres----------
        if retourcategorie == 'Books':
            soup = BeautifulSoup(reponse.text, "html.parser")
            page = soup.find('li', {'class': 'next'}).find('a')
            nombrepage = soup.find('li', {'class': 'current'}).text
            pagesansespace = nombrepage.strip()
            totalpage = pagesansespace[10:]
            pagetotal = int(totalpage) - 2
            urlpagenext = page['href']
            books = []
            newurl = "https://books.toscrape.com/catalogue/category/books_1/" + urlpagenext
            books.append("https://books.toscrape.com/catalogue/category/books_1/index.html")
            books.append(newurl)
            for i in range(pagetotal):
                newurl = "https://books.toscrape.com/catalogue/category/books_1/" + urlpagenext
                newresponse = requests.get(newurl)
                soups = BeautifulSoup(newresponse.text, "html.parser")
                pages = soups.find('li', {'class': 'next'}).find('a')
                urlpagenext = pages['href']
                newurl = "https://books.toscrape.com/catalogue/category/books_1/" + urlpagenext
                books.append(newurl)
            for l in books:
                r = requests.get(l)
                s = BeautifulSoup(r.text, "html.parser")
                liste = s.findAll('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
                for li in liste:
                    a = li.find('a')
                    resultatbrut = a["href"]
                    resultatbrut = re.sub('[..]', '', resultatbrut)
                    resultatpropre = resultatbrut[2:]
                    link2 = resultatpropre[:-4]
                    links.append('https://books.toscrape.com/catalogue/' + link2 + '.html')
            print("")
            print('il y a : ' + str(len(links)) + ' livres au total sur le site.')
    # fin du rajout de code ---------------------------------------------------------------
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            liste = soup.findAll('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
            nomberbooks = soup.find('form', {'class': 'form-horizontal'}).find('strong').text
            if int(nomberbooks) > 20:
                pages = soup.find('li', {'class': 'next'}).find('a')
                pages2 = pages['href']
                pagenext = url[:-10]
                liens = (pagenext + pages2)
                reponses = requests.get(liens)
                soups = BeautifulSoup(reponses.text, 'html.parser')
                page = soup.find('li', {'class': 'next'}).find('a')
                nombrepage = soup.find('li', {'class': 'current'}).text
                pagesansespace = nombrepage.strip()
                totalpage = pagesansespace[10:]
                pagetotal = int(totalpage) -2
                urlpagenext = page['href']
                newurl2 = newurls[:-10]
                link = []
                link.append(newurls)
                link.append(newurl2 + urlpagenext)
                for i in range(pagetotal):
                    newurl = newurl2 + urlpagenext
                    newresponse = requests.get(newurl)
                    soups = BeautifulSoup(newresponse.text, "html.parser")
                    pages = soups.find('li', {'class': 'next'}).find('a')
                    urlpagenext = pages['href']
                    newurl = newurl2 + urlpagenext
                    link.append(newurl)
                for l in link:
                    r = requests.get(l)
                    s = BeautifulSoup(r.text, "html.parser")
                    liste1 = s.findAll('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
                    for li in liste1:
                        a = li.find('a')
                        resultatbrut = a["href"]
                        resultatbrut = re.sub('[..]', '', resultatbrut)
                        resultatpropre = resultatbrut[2:]
                        link2 = resultatpropre[:-4]
                        links.append('https://books.toscrape.com/catalogue' + link2 + '.html')
                print("")
                print('il y a : ' + str(len(links)) + ' livres dans la selection: '+ retourcategorie)
            else:
                for li in liste:
                    a = li.find('a')
                    resultatbrut = a["href"]
                    resultatbrut = re.sub('[..]', '', resultatbrut)
                    resultatpropre = resultatbrut[2:]
                    link = resultatpropre[:-4]
                    links.append('https://books.toscrape.com/catalogue' + link + '.html')
                print("")
                print('il y a : ' + str(len(links)) + ' livres dans la selection: '+ retourcategorie)
    return links


# fonction de srappe de la totalité des images et extraites par categories
def recherche_totalite_images(links, category):
    del links["Books"]
    del category[0]
    for i in links:
        link = links.get(i)
        categorie = i
        retour = recherche_categorie(link, categorie)
        details = recherche_infos_book(retour)
        enregistrement_des_images(details)


# fonction de gestion de srcappe de la totalité des livres et extraites par categorie
def recherche_totalite_infos(links, category):
    del links["Books"]
    del category[0]
    for i in links:
        link = links.get(i)
        categorie = i
        retour = recherche_categorie(link, categorie)
        details = recherche_infos_book(retour)
        impression_du_details(details)