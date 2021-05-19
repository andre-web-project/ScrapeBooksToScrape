import os
import urllib.request as ulib


# creation fonction de requette de url des images
def get_html(source):
    with ulib.urlopen(source) as u:
        return u.read()


# creation fonction pour l'impression du detail et l'enregistrement des images
def enregistrement_des_images(valeurs):
    images = []
    simple = valeurs[0]
    categ = simple[5]
    for i in valeurs:
        image = i[-1]
        images.append(image)
    entre = input('Voulez vous enregistrer les images ? ')
    validation = entre.lower()
    # creation du dossier pour accueillir les images
    if validation == "oui":
        if not os.path.exists("imagesCouv" + categ):
            os.makedirs("imagesCouv" + categ)
        for i, img in enumerate(images):
            nom = img.split("/")[-1]
            dest = os.path.join("imagesCouv" + categ, nom)
            if os.path.exists(dest):
                continue
            try:
                contenu = get_html(img)
            except Exception as e:
                continue
            with open(dest, "wb") as f:
                f.write(contenu)
        print("Les images ont etaient enregistrées .")
        print("")
    else:
        print("Fin de la recherche.")
        print("")

