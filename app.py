import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

# Charger les données
def load_data():
    df = pd.read_csv("data/melb_data.csv")
    df.dropna(subset=["Price", "Landsize", "YearBuilt", "BuildingArea", "Suburb"], inplace=True)
    df = df[(df["Price"] > 10000) & (df["Landsize"] > 0)]  # Suppression des valeurs aberrantes
    return df

df = load_data()

# Identifier les colonnes clés
key_columns = ["Price", "Suburb", "Landsize", "YearBuilt", "BuildingArea"]

# Création des onglets
st.title("🏡 Dashboard Immobilier - Melbourne Housing")
st.markdown("Ce dashboard interactif permet d'explorer et d'analyser les tendances du marché immobilier de Melbourne.")

tabs = st.tabs(["Aperçu des données", "Statistiques", "Visualisations", "Prédictions"])

with tabs[0]:
    st.subheader("Aperçu des données")
    st.write(df.head())

with tabs[1]:
    # Calculer des statistiques descriptives
    st.subheader("Statistiques descriptives")
    st.write(df[key_columns].describe())

# Filtres interactifs
st.sidebar.header("Filtres")
prix_min, prix_max = st.sidebar.slider("Plage de prix", int(df["Price"].min()), int(df["Price"].max()), (int(df["Price"].min()), int(df["Price"].max())))
ville = st.sidebar.multiselect("Sélectionner la ville", df["Suburb"].unique(), default=df["Suburb"].unique())
annee_min, annee_max = st.sidebar.slider("Année de construction", int(df["YearBuilt"].min()), int(df["YearBuilt"].max()), (int(df["YearBuilt"].min()), int(df["YearBuilt"].max())))

# Filtrer les données
filtered_df = df[(df["Price"] >= prix_min) & (df["Price"] <= prix_max) &
                 (df["Suburb"].isin(ville)) &
                 (df["YearBuilt"] >= annee_min) & (df["YearBuilt"] <= annee_max)]

with tabs[2]:
    st.subheader("Données filtrées")
    st.write(filtered_df.head())

    # Histogramme des prix
    st.subheader("Distribution des prix")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df["Price"], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

    # Graphique en barres des ventes par année
    st.subheader("Ventes par année")
    fig_bar, ax = plt.subplots()
    sns.countplot(x=filtered_df["YearBuilt"], ax=ax, order=filtered_df["YearBuilt"].value_counts().index[:20])
    plt.xticks(rotation=90)
    st.pyplot(fig_bar)

    # Carte des ventes
    st.subheader("Carte des ventes")
    fig_map = px.scatter_mapbox(filtered_df, lat="Lattitude", lon="Longtitude", color="Price",
                                size=np.log(filtered_df["Price"]), hover_name="Suburb", zoom=10,
                                mapbox_style="carto-positron")
    st.plotly_chart(fig_map)

    # Heatmap des corrélations
    st.subheader("Corrélations entre les caractéristiques")
    corr_matrix = df[["Price", "Landsize", "BuildingArea", "YearBuilt"]].corr()
    fig_corr, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig_corr)

with tabs[3]:
    # Modèle de prédiction
    st.subheader("Prédiction du prix")
    features = ["Landsize", "YearBuilt", "BuildingArea"]
    X = filtered_df[features]
    y = filtered_df["Price"]
    model = LinearRegression()
    model.fit(X, y)
    prediction = model.predict(X)
    st.write("### Exemples de prédictions :")
    st.write(pd.DataFrame({"Prix réel": y.values[:5], "Prix prédit": prediction[:5]}))

    # Analyse des facteurs influençant les prix
    st.subheader("Importance des caractéristiques")
    importance = pd.Series(model.coef_, index=features).sort_values(ascending=False)
    st.bar_chart(importance)

st.markdown("### 🔍 Insights clés")
st.write("- Les prix varient fortement selon la localisation.", "\n- La taille du terrain, l'année de construction et la surface du bâtiment influencent les prix.")
