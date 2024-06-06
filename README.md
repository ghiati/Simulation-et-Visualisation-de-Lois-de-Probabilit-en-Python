# Simulation et Visualisation de Lois de Probabilité en Python

Ce projet propose des simulations de différentes lois de probabilité et la visualisation de leurs résultats à l'aide de Python et Jupyter Notebook.

## Structure du Projet

```plaintext
Simulation-et-Visualisation-de-Lois-de-Probabilite-en-Python/
│
├── probabilite_lois.py          # Contient les fonctions de simulation des lois de probabilité
├── principal.py                 # Menu interactif pour choisir et exécuter des simulations
├── visualisation_notebook.ipynb # Notebook Jupyter pour visualiser les résultats des simulations
└── README.md                    # Documentation du projet
```

### Contenu des Fichiers

#### `probabilite_lois.py`
Ce fichier contient des fonctions pour la simulation des lois de probabilité. Chaque fonction simule une loi spécifique comme la loi de Bernoulli, la loi binomiale, la loi géométrique, etc.

#### `principal.py`
Ce fichier contient un menu interactif qui permet à l'utilisateur de choisir la loi de probabilité à simuler, de saisir les paramètres nécessaires, et d'exécuter la simulation. Les résultats de la simulation sont affichés à l'écran.

#### `visualisation_notebook.ipynb`
Ce notebook Jupyter contient des exemples de visualisation des résultats des simulations à l'aide de graphiques générés avec la bibliothèque Matplotlib.

## Utilisation

1. **Cloner le Repository** :
   ```sh
   git clone https://github.com/ghiati/Simulation-et-Visualisation-de-Lois-de-Probabilite-en-Python.git
   ```

2. **Accéder au Répertoire du Projet** :
   ```sh
   cd Simulation-et-Visualisation-de-Lois-de-Probabilite-en-Python
   ```

3. **Installer les Dépendances** :
   Assurez-vous d'avoir Python installé sur votre système, puis exécutez :
   ```sh
   pip install matplotlib
   ```

4. **Exécuter le Menu Interactif** :
   Pour lancer le menu interactif et exécuter des simulations, exécutez :
   ```sh
   python principal.py
   ```

5. **Visualisation avec Jupyter Notebook** :
   - Lancez Jupyter Notebook :
     ```sh
     jupyter notebook visualisation_notebook.ipynb
     ```
   - Exécutez les cellules pour visualiser les graphiques des résultats des simulations.

## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, suivez ces étapes :
1. Fork ce repository
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/nom-de-la-fonctionnalite`)
3. Committez vos modifications (`git commit -am 'Ajout de la fonctionnalité'`)
4. Poussez la branche (`git push origin feature/nom-de-la-fonctionnalite`)
5. Ouvrez une Pull Request


