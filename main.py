import requests
from bs4 import BeautifulSoup
import codecs

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

reponse = requests.get(url)

if reponse.ok:
    soup = BeautifulSoup(reponse.text, "lxml")

    tds = soup.findAll('td')

    title = soup.find("h1").text
    price_including_tax = tds[3].text
    print("price_including_tax", price_including_tax)
    price_excluding_tax = tds[2].text
    print("price_excoding", price_excluding_tax)
    number_available = tds[5].text
    product_description = tds[1].text
    category = soup.findAll('a')[3].text
    review_rating = soup.find('p', class_='star-rating')['class'][1].lower()
    image_url = soup.find('img')['src']

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
valeurs = [
    title,
    price_including_tax,
    price_excluding_tax,
    number_available,
    product_description,
    category,
    review_rating,
    image_url
]
ligneEntete = ';'.join(entetes) + '\n'
ligne = ";".join(valeurs) + "\n"

with codecs.open('scrappingBooks.csv', 'w', encoding='utf-8') as file:
    file.write(ligneEntete)
    file.write(ligne)
