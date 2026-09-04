import streamlit as st
import joblib

model = joblib.load("regression.joblib")

taille = st.number_input("Taille de la maison (en m²)", min_value=0.0, value=100.0)
chambres = st.number_input("Nombre de chambres", min_value=0, value=3, step=1)
jardin = st.number_input("Présence d'un jardin (0 = Non, 1 = Oui)", min_value=0, max_value=1, value=0, step=1)

caracteristiques = [[taille, chambres, jardin]]

prediction = model.predict(caracteristiques)

st.write(f"Le prix estimé pour cette maison est de : {prediction[0]:.2f}")