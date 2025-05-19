import streamlit as st
import pandas as pd
import json
import os
from requerimiento2 import estadisticas_generales
from requerimiento3 import analyze_category_frequencies
from requerimiento5 import count_frequencies
import categorias

# Título
st.title("Despliegue Proyecto Final - Análisis de Algoritmos")

# Cargar datos
st.header("Cargar archivo JSON procesado")
with open("processed_articles.json", encoding="utf-8") as f:
    data = json.load(f)
    st.success("Archivo cargado correctamente.")

# Mostrar una muestra del dataset
if st.checkbox("Mostrar artículos procesados"):
    st.json(data[:3])

# Requerimiento 2: Estadísticas Generales
st.header("Estadísticas Generales (Requerimiento 2)")
if st.button("Generar estadísticas"):
    estadisticas_generales(data)

# Requerimiento 3: Frecuencia de categorías y nube de palabras
st.header("Frecuencia de categorías y Nube de Palabras (Requerimiento 3)")
if st.button("Analizar categorías"):
    analyze_category_frequencies(data)

# Requerimiento 5: Agrupamiento por similitud
st.header("Similitud entre abstracts (Requerimiento 5)")
if st.button("Calcular similitudes"):
    count_frequencies(data)

# Categorías
st.sidebar.title("Categorías")
st.sidebar.write(categorias.obtener_categorias())
