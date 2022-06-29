# Selenium-Twitter

Bot Twitter utilisant Selenium.

## Dépendance du script :

Vous devez installer cette librarie python3 pour que le script fonctionne :
```
selenium==4.1.5
```

## Installation :

* Installation de ChromeDriver : [chromedriver](https://chromedriver.chromium.org/getting-started)

* Vous devez ensuite installer une version 3.x de Python : [Python 3.x](https://www.python.org/downloads/)

* Pour finir vous devez installer la librairie selenium :
     ```
     python3 -m pip install selenium
     ou
     py -m pip install selenium
     ```
Ces commandes sont à rentrer dans votre console (cmd pour Windows)
Si pip n'est pas reconnu vous devez l'installer.

## Configuration :

Tous les paramètres de configurations sont dans le fichier **configuration.yml**.  
Copiez le fichier **configuration.yml.tpl** pour créer le fichier **configuration.yml**.

Vous devez renseigner votre nom d'utilisateur et votre mot de passe Twitter :
```
account:
    username : ""
    password : ""    
```
Il faut mettre votre compte Twitter en Francais.


## Lancement :
```
python3 main.py
ou
py main.py
```
