import streamlit as st
import pandas as pd
import json
import os
from requerimiento2 import estadisticas_generales
from requerimiento3 import analyze_category_frequencies
from requerimiento5 import calcular_similitud_entre_abstracts
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

    # Mostrar visualizaciones del Requerimiento 2
    st.subheader("Visualizaciones del Requerimiento 2")
    imagenes_req2 = [
        "2_yearly_trends.png",
        "2_top_authors.png",
        "2top_journals.png",
    ]
    for imagen in imagenes_req2:
        ruta = os.path.join("resultados", imagen)
        if os.path.exists(ruta):
            st.image(ruta, caption=imagen.replace("_", " ").replace(".png", ""), use_column_width=True)
        else:
            st.warning(f"No se encontró la imagen: {imagen}")

# Requerimiento 3: Frecuencia de categorías y Nube de Palabras
st.header("Frecuencia de categorías y Nube de Palabras (Requerimiento 3)")
if st.button("Analizar categorías"):
    analyze_category_frequencies(data)
    st.success("Frecuencias analizadas correctamente.")

    # Mostrar gráficos generados para cada categoría
    st.subheader("Visualización por Categoría")
    for categoria in categorias.CATEGORIAS.keys():
        imagen_barra = os.path.join("resultados", f"3_{categoria}_frecuencia.png")
        imagen_nube = os.path.join("resultados", f"3_{categoria}_wordcloud.png")
        if os.path.exists(imagen_barra):
            st.image(imagen_barra, caption=f"Frecuencia en {categoria}", use_column_width=True)
        if os.path.exists(imagen_nube):
            st.image(imagen_nube, caption=f"Nube de Palabras en {categoria}", use_column_width=True)

    # Mostrar nubes y co-word general
    imagen_general_nube = os.path.join("resultados", "3_wordcloud_general.png")
    imagen_co_word = os.path.join("resultados", "3_co_word_network.png")
    if os.path.exists(imagen_general_nube):
        st.image(imagen_general_nube, caption="Nube de Palabras General", use_column_width=True)
    if os.path.exists(imagen_co_word):
        st.image(imagen_co_word, caption="Co-word Network", use_column_width=True)

# Requerimiento 5: Agrupamiento por similitud
st.header("Similitud entre abstracts (Requerimiento 5)")
if st.button("Calcular similitudes"):
    calcular_similitud_entre_abstracts(data)
    st.success("Similitudes calculadas correctamente.")

    # Mostrar dendrogramas generados
    st.subheader("Dendrogramas de Agrupamiento")
    dendrogramas = ["dendrogram_average.png", "dendrogram_ward.png"]
    for img in dendrogramas:
        ruta_img = os.path.join("resultados", img)
        if os.path.exists(ruta_img):
            st.image(ruta_img, caption=img.replace("_", " ").replace(".png", ""), use_column_width=True)
        else:
            st.warning(f"No se encontró la imagen: {img}")

# Mostrar selector de categorías en el sidebar
st.sidebar.subheader("Selecciona una categoría")
categoria_seleccionada = st.sidebar.selectbox(
    "Categorías disponibles",
    list(categorias.CATEGORIAS.keys())
)

st.write(f"Has seleccionado la categoría: **{categoria_seleccionada}**")
st.write("Elementos de la categoría seleccionada:")
for item in categorias.CATEGORIAS[categoria_seleccionada]:
    st.markdown(f"- {item}")
