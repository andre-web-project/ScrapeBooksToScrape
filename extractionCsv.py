import csv


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
    ligneentete = ';'.join(entetes) + '\n'
    if int(nombre) == 1:
        with open('scrappingBooks' + valeurs[5] + '.csv', 'w', newline="", encoding='utf-8') as file:
            file.write(ligneentete)
            writer = csv.writer(file, delimiter=';')
            for row in valeur:
                writer.writerow(row)
        print("Le fichier csv a était généré.")
        print("")
    elif 1 < int(nombre) < 900:
        with open('scrappingBooks' + valeurs[5] + '.csv', 'w', newline="", encoding='utf-8') as file:
            file.write(ligneentete)
            writer = csv.writer(file, delimiter=';')
            for row in valeur:
                writer.writerow(row)
        print("Le fichier csv a était généré.")
        print("")
    else:
        for i in valeur:
            cat = i[5]
            with open('scrappingBooks' + cat + '.csv', 'w', newline="", encoding='utf-8') as file:
                file.write(ligneentete)
                writer = csv.writer(file, delimiter=';')
                for row in valeur:
                    writer.writerow(row)
        print("Le fichier csv a était généré.")
        print("")