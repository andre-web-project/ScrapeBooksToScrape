import requests
from bs4 import BeautifulSoup
import os

url ="https://books.toscrape.com/media/cache/c0/59/c05972805aa7201171b8fc71a5b00292.jpg"
reponse = requests.get(url)

if not os.path.exists("books.toscrape"):
    os.makedirs("books.toscrape")
    for i, img in enumerate(images):
        nom = img.split("/")[-1]
        dest = os.path.join("images/lemonde2", nom)
        if os.path.exists(dest):
            continue

        try:
            contenu = get_html(img)
        except Exception as e:
            print(e)
            continue
        print(f"{i + 1}/{len(images)}: {nom}")
        with open(dest, "wb") as f:
            f.write(contenu)