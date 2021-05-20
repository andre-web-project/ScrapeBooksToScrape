import codecs


# fonction le creation de fichier csv
def impression_du_details(valeur):
    nombre = len(valeur)
    valeurs = valeur[0]
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
    ligneEntete = ';'.join(entetes) + '\n'
    if int(nombre) == 1:
        with codecs.open('scrappingBooks' + valeurs[0] + '.csv', 'w', encoding='utf-8') as file:
            file.write(ligneEntete)
            for row in valeur:
                ligne = ';'.join(row) + '\n'
                file.write(ligne)
        print("Le fichier csv a était généré.")
        print("")
    elif 1 < int(nombre) < 900:
        with codecs.open('scrappingBooks' + valeurs[5] + '.csv', 'w', encoding='utf-8') as file:
            file.write(ligneEntete)
            for row in valeur:
                ligne = ';'.join(row) + '\n'
                file.write(ligne)
        print("Le fichier csv a était généré.")
        print("")
    else:
        for i in valeur:
            cat = i[5]
            with codecs.open('scrappingBooks' + cat + '.csv', 'w', encoding='utf-8') as file:
                file.write(ligneEntete)
                for row in valeur:
                    ligne = ';'.join(row) + '\n'
                    file.write(ligne)
        print("Le fichier csv a était généré.")
        print("")