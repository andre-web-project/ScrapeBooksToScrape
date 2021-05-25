import os
import urllib.request as ulib


# creation fonction de requette de url des images
def get_html(source):
    with ulib.urlopen(source) as u:
        return u.read()


# creation fonction pour l'enregistrement des images
def enregistrement_des_images(valeurs):
    images = []
    names = []
    simple = valeurs[0]
    categ = simple[5]
    for i in valeurs:
        image = i[-1]
        name = i[0]
        images.append(image)
        names.append(name)
    # creation du dossier pour stocker les images
    if not os.path.exists("imagesCouv" + categ):
        os.makedirs("imagesCouv" + categ)
    for i, img in zip(names, images):
        nom = i + ".jpg"
        dest = os.path.join("imagesCouv" + categ, nom)
        print(dest)
        if os.path.exists(dest):
            continue
        try:
            contenu = get_html(img)
        except Exception as e:
                continue
        with open(dest, "wb") as f:
            f.write(contenu)
    print("Les images ont étaient enregistrées .")
    print("")


