Dashboard Immobilier - Melbourne Housing

🏠 Description:
Ce projet est une application interactive développée avec Streamlit permettant d'explorer et d'analyser les tendances du marché immobilier de Melbourne. L'application offre des visualisations dynamiques et des statistiques pour aider à mieux comprendre l'évolution des prix, la distribution géographique des biens et les facteurs influençant les prix.

🚀 Fonctionnalités principales:
-Affichage des données : Vue d'ensemble des annonces immobilières de Melbourne.
-Statistiques descriptives : Moyennes, médianes et distributions des prix et des surfaces.
-Visualisations interactives : Données filtrées, Histogrammes, cartes géographiques et heatmaps des corrélations.
-Prédiction des prix : Modèle de régression linéaire pour estimer les prix des biens.

📌 Prérequis
Assurez-vous d'avoir installé les éléments suivants sur votre machine :
 -Python (>= 3.7)
 -Les bibliothèques Python nécessaires : streamlit, pandas, matplotlib, seaborn, plotly, scikit-learn

📊 Données utilisées
-Fichier : melb_data.csv
-Colonnes clés : Price, Landsize, YearBuilt, BuildingArea, Suburb
-Nettoyage des données : Suppression des valeurs aberrantes et des données manquantes.

🎨 Visualisations incluses
-Distribution des prix : Histogramme des prix des biens.
-Ventes par année : Graphique des ventes en fonction de l'année de construction.
-Carte interactive : Localisation des biens en fonction de leur prix.
-Heatmap des corrélations : Analyse des relations entre différentes variables.

▶️ Exécution
Lancez l'application avec la commande suivante :
    streamlit run app.py 