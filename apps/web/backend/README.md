# Backend de l'application Dice Arèna

## Solution dockerisé avec :
    . python flask
    . mongoDB

## Pour lancer la partie backend :
Se rendre dans le répertoire backend et lancer la commande suivante depuis le terminal
>docker-compose up -d


### notes perso
dans le fichier main.py
=> install Cors : pip install -U flask-cors
+ ajout aux requirements

### modification du fichier main.py
en cas de modification du fichier main.py
rebuilder d'abord l'image docker pour prendre en compte les modifications
>docker-compose build --no-cache

ensuite lancer docker-compose
>docker-compose up -d

