import streamlit as st
import pandas as pd
import json
import os
from requerimiento2 import estadisticas_generales
from requerimiento3 import analyze_category_frequencies
from requerimiento5 import calcular_similitud_entre_abstracts
import categorias 
from flask import Flask, render_template

# Título
st.title("Despliegue Proyecto Final - Análisis de Algoritmos")

# Cargar datos
st.header("Cargar archivo JSON procesado")
with open("processed_articles.json", encoding="utf-8") as f:
    data = json.load(f)
    st.success("Archivo cargado correctamente.")

# Mostrar una muestra del dataset
if st.checkbox("Mostrar artículos procesados"):
    st.json(data[:100])

# Requerimiento 2: Estadísticas Generales
st.title("Estadísticas Generales (Requerimiento 2)")

uploaded_file = st.file_uploader("Sube el archivo JSON procesado", type="json")

if uploaded_file:
    try:
        data = json.load(uploaded_file)
        data = data[:1000]  # limitar si es necesario
        estadisticas_generales(data)
        st.success("Estadísticas generadas correctamente.")
    except Exception as e:
        st.error(f"Error al procesar el archivo JSON: {e}")

app = Flask(__name__)

@app.route("/")
def index():
    # Lista de imágenes que se encuentran en static/img/
    imagenes = [
        "3_Herramienta_frecuencia.png",
        "3_Actitudes_frecuencia.png",
        "3_Conceptos Computacionales_frecuencia.png",
        "3_Diseño de Investigación_frecuencia.png",
        "3_Estrategia_frecuencia.png",
        "3_Habilidades_frecuencia.png",
        "3_Herramienta de Evaluación_frecuencia.png"
    ]
    return render_template("index.html", imagenes=imagenes)

if __name__ == "__main__":
    app.run(debug=True)

# Requerimiento 3: Frecuencia de categorías y nube de palabras
st.header("Frecuencia de categorías y Nube de Palabras (Requerimiento 3)")
if st.button("Analizar categorías"):
    analyze_category_frequencies(data)

# Requerimiento 5: Agrupamiento por similitud
st.header("Similitud entre abstracts (Requerimiento 5)")
if st.button("Calcular similitudes"):
    calcular_similitud_entre_abstracts(data)

# Mostrar selector de categorías en el sidebar
st.sidebar.subheader("Selecciona una categoría")
categoria_seleccionada = st.sidebar.selectbox(
    "Categorías disponibles",
    list(categorias.CATEGORIAS.keys())  # esto reemplaza a obtener_categorias si no existe
)

st.write(f"Has seleccionado la categoría: **{categoria_seleccionada}**")
st.write("Elementos de la categoría seleccionada:")
for item in categorias.CATEGORIAS[categoria_seleccionada]:
    st.markdown(f"- {item}")
