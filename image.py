from main import impressionDuDetails
import os
import urllib.request as ulib


def get_html(source):
    with ulib.urlopen(source) as u:
        return u.read()

images = impressionDuDetails()

if not os.path.exists("imagesCouv"):
    os.makedirs("imagesCouv")
for i, img in enumerate(images):
    nom = img.split("/")[-1]
    dest = os.path.join("imagesCouv", nom)
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