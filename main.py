from scrappe import recherche_infos_book, recherche_categorie, choix_categorie
from extractionCsv import impression_du_details
from enregistrementPic import enregistrement_des_images


# fonction menu pour l'accueil de l'application et la gestion des choix
def menu_accueil():
    print("")
    print("Bienvenue sur votre application de veille marketing du site Books to scrape.")
    print("")
    print("Tapez 1 : pour extraire toutes les informations d'un livre en retrant son url.")
    print("Tapez 2 : pour extraire tous les liens et informations des livres d'une catégorie choisit.")
    print("Tapez 3 : pour extraire la totalité des informations du sites")
    print("Tapez 4 : pour enregistrer les images de livres.")
    print("Tapez 5 : pour fermer l'application.")
    choix = input(":  ")
    # 1 choix url en console > srapping des infos > fichier csv
    if choix == "1":
        print("Veuillez saisir une url valide ")
        url = [input(": ")]
        valeurs = recherche_infos_book(url)
        print("les données du livre ont étaient recuperées avec succés.")
        impression_du_details(valeurs)
    # 2 choix affichage des categories puis choix en console > scrapping des infos > fichier csv des liens des livres > fichier csv des informations
    elif choix == "2":
        retour = choix_categorie()
        liens = retour[0]
        categorie = retour[1]
        valeurs = recherche_categorie(liens, categorie)
        details = recherche_infos_book(valeurs)
        impression_du_details(details)
    #  choix  > scrapping de toutes les infos > fichier csv  des liens > fichier csv des informations
    elif choix == "3":
        liens = "https://books.toscrape.com/catalogue/category/books_1/index.html"
        categorie = "Books"
        valeurs = recherche_categorie(liens, categorie)
        details = recherche_infos_book(valeurs)
        impression_du_details(details)
    #  choix  > affichage des categories puis choix en console > creation d'un dossier et enregistrement des images
    elif choix == "4":
        retour = choix_categorie()
        liens = retour[0]
        categorie = retour[1]
        valeurs = recherche_categorie(liens, categorie)
        details = recherche_infos_book(valeurs)
        impression_du_details(details)
        enregistrement_des_images(details)
    # sortie du proramme
    elif choix == "5":
        print("Fin de recherche.")
        print("")
    # gestion des cas d'erreurs
    else:
        print("Erreur ! vous devez selectionner un menu existant")
        return menu_accueil()


menu_accueil()