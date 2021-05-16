import requests
from bs4 import BeautifulSoup
import codecs
import re

url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
reponse = requests.get(url)
link = []
links = []

if reponse.ok:
    soup = BeautifulSoup(reponse.text,"html.parser")
    page = soup.find('li', {'class': 'next'}).find('a')
    nombrePage = soup.find('li', {'class': 'current'}).text
    pageSansEspace = nombrePage.strip()
    totalPage = pageSansEspace[10:]
    pageTotal = int(totalPage) - 2
    urlPageNext = page['href']
    newUrl = "https://books.toscrape.com/catalogue/category/books_1/" + urlPageNext
    link.append(url)
    link.append(newUrl)
    for i in range(pageTotal):
        newUrl = "https://books.toscrape.com/catalogue/category/books_1/" + urlPageNext
        newResponse = requests.get(newUrl)
        soups = BeautifulSoup(newResponse.text, "lxml")
        pages = soups.find('li', {'class': 'next'}).find('a')
        urlPageNext = pages['href']
        newUrl = "https://books.toscrape.com/catalogue/category/books_1/" + urlPageNext
        link.append(newUrl)
for l in link:
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

print(len(links))

