# Config `.env` to django project

Configuration des variables d'environnement dans un projet Django

## Table des matières

-   [Installation](#installation)
-   [Utilisation](#utilisation)
-   [Contribuer](#contribuer)
-   [Licence](#licence)

## Installation

Assurez-vous d'avoir `Python` installé. Clonez ce dépôt sur votre machine locale en utilisant la commande suivante :

```bash
$ git clone git@github.com:nbesoro/python-env-variable.git
```

Créez un environnement virtuel pour isoler les dépendances du projet (si vous ne l'avez pas déjà fait) :

```bash
$ python -m venv venv
```

Activez l'environnement virtuel (selon votre système d'exploitation) :

Sur Windows :

```bash
$ venv\Scripts\activate
```
Sur macOS et Linux :

```bash
$ source venv/bin/activate
```


Installez les dépendances en exécutant la commande suivante :

```bash
$ pip install -r requirements.txt
```

## Utilisation

Lancez le serveur de développement avec la commande :

```bash
$ python manage.py runserver
```

Ouvrez votre navigateur et accédez à [http://localhost:8000](http://localhost:8000).

## Contribuer

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

## Licence

Ce projet est sous licence [MIT](https://choosealicense.com/licenses/mit/).

---

© [Nbe Soro](https://nbesoro.com)
