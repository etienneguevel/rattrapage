# Rattrapage cours Python ISUP 2024 / 2025

Ce repo contient le sujet pour le rattrapage de l'ISUP 2024/2025.  
Ce projet vise à analyser des données de matchs et de joueurs de la NBA (
National Basketball Association), et de permettre à un utilisateur de chercher
des statistiques d'intérêts sur ces données.

## Données

Les données sont contenues dans plusieurs fichiers `.csv` :

- `Players.csv`: contient des informations générales sur le joueur
- `PlayerStatistics.csv`: contient les statistiques d'un joueur sur un match
- `TeamStatistics.csv`: contient les statistiques d'une équipe sur un match
- `Salaries.csv`: contient les salaires sur plusieurs saisons de **certains
    joueurs** uniquement

La colonne `personId` est l'identifiant unique de chaque joueur, `gameId` est
l'identifiant unique de chaque match.

## Consignes

Le but est de créer un package python, avec un fichier `README.md` (comme 
celui-ci) décrivant le projet, et un setup permettant l'installation de votre
code comme un package (ie si je fais `pip install .` j'ai votre package installé
dans mon env python).  
Le setup peut se faire avec des fichiers `setup.py` ou `pyproject.toml` au choix.

Ce package devra remplir 3 objectifs principaux.  

### 1. Observer le leaderboard des joueurs sur une catégorie statistique

Le package python devra contenir un script qui permettra à l'utilisateur de
pouvoir observer les meilleurs joueurs dans la catégorie statistiques choisie 
(points, rebonds...).  

Voir le fichier `src/rattrapage/statistics.py` pour un example.

### 2. Observer les statistiques d'une équipe sur une saison

Le package python devra aussi avoir un autre script permettant d'afficher les
statistiques de l'équipe choisie lors d'une saison.  
Le script affichera aussi les membres de cette équipe lors de cette saison,
ainsi que leurs statistiques pendant cette saison.

Voir le fichier `src/rattrapage/team_statistics.py` pour un example.

### 3. Prédire le salaire d'un joueur

Pour les joueurs étant présent dans le fichier `Salaries.csv` cette partie vise
à créer une classe python permettant de faire de la régression linéaire sur
les statistiques des joueurs.

Les étapes sont les suivantes:

- Calculer les métriques pour ces joueurs (moyennes des statistiques)
- Créer une `class` python `LinearRegression` avec :
    - méthode `fit` sur les données d'entraînements
    - méthode `predict` sur de nouvelles données et renvoie la prédiction
    - méthode `get_coeffs` renvoie les valeurs des coefficients associés
    - argument en entrée `intercept` booléen indiquant si il y a une variable
        constante dans la modélisation
- Plot les résultats, selon votre choix

## Restrictions

Les librairies autorisées pour ce projet sont : `pandas`, `numpy`, `matplotlib`
et `seaborn`. D'autres librairies de visualisation sont tolérées (exemple
`tabulate`), mais des librairies comme `sklearn` ou `statsmodels` sont
proscrites.

