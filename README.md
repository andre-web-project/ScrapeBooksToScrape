# ScrapeBooksToScrape
Application de veille marketing d'une librairie en ligne.

L'application ,en plus de ce fichier README, ce compose de:
			     - 4 scripts python.
			     - 1 fichier requirements.txt ( ressources pip nécessaires a installer dans votre environement virtuel ). 
			     - 1 fichier .gitignore ( sert a exclure les fichiers non pris en charge par git ).

Etape 1 :
	Mise en place de votre environement virtuel.
	- Dans votre terminal, allez dans le repertoire où se situe le dossier qui contient tout les fichiers et srcipts de l'application.
	- Créez votre environement virtuel en tapant : sur windows :        python -m venv env
						       sur mac ou Unix :    python3 -m venv env

	- En cas de besoin, vous trouverez plus d'informations sur docs.python liens ci-joins : 
									    https://docs.python.org/fr/3/library/venv.html

	- Activez votre environement en tapant : sur windows :              env\scripts\activate
						sur mac ou Unix :           source env/bin/activate

	- Vous allez voir apparaitre "(env)" en entête de la ligne de commande. 

Etape 2 :
	Integration des bibliothèques nécesaires pour l'application.
	- Dans votre environement virtuel que vous venez de créer, importez toutes les bibliothèques nécesaires en tapant :
								  	    pip install -r requirements.txt            

Etape 3 : 
	L'application est prête vous pouvez la lancer en tapant :
								  python main.py

	- L'application vous demandera de selectionner une catégorie afin de recuperer l'ensemble ces données dans la librairie.
	- L'application générera un fichier csv avec tout les livres de la selection.
	- Ensuite elle vous demandera si vous voulez extraire des données plus detaillées ainsi que les images de couverture.

