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
        # Mostrar visualizaciones del Requerimiento 2
        st.subheader("Visualizaciones del Requerimiento 2")

imagenes_req2 = [
    "2_yearly_trends.png",
    "2_top_authors.png",
    "2top_journals.png",
]

for imagen in imagenes_req2:
    ruta = os.path.join("data", imagen)
    if os.path.exists(ruta):
        st.image(ruta, caption=imagen.replace("_", " ").replace(".png", ""), use_column_width=True)
    else:
        st.warning(f"No se encontró la imagen: {imagen}")
        st.success("Estadísticas generadas correctamente.")
    except Exception as e:
        st.error(f"Error al procesar el archivo JSON: {e}")


# Requerimiento 3: Frecuencia de categorías y nube de palabras
st.header("Frecuencia de categorías y Nube de Palabras (Requerimiento 3)")
if st.button("Analizar categorías"):
    analyze_category_frequencies(data)
# Mostrar imágenes generadas para Requerimiento 3
st.header("Visualización de Imágenes de Frecuencia por Categoría")

# Mostrar visualizaciones generadas del Requerimiento 3
st.header("Visualizaciones de Requerimiento 3")

image_folder = "resultados"  # Asegúrate que existan allí las imágenes

# Listas de imágenes a mostrar
bar_images = [
    "3_Herramienta_frecuencia.png",
    "3_Actitudes_frecuencia.png",
    "3_Conceptos Computacionales_frecuencia.png",
    "3_Diseño de Investigación_frecuencia.png",
    "3_Estrategia_frecuencia.png",
    "3_Habilidades_frecuencia.png",
    "3_Herramienta de Evaluación_frecuencia.png",
    "3_Herramienta_frecuencia.png",
    "3_Medio_frecuencia.png",
    "3_Nivel de Escolaridad_frecuencia.png",
    "3_Propiedades Psicométricas_frecuencia.png",
    
]

wordcloud_images = [
    "3_Herramienta_wordcloud.png",
    "3_Actitudes_wordcloud.png",
    "3_Conceptos Computacionales_wordcloud.png",
    "3_Diseño de Investigación_wordcloud.png",
    "3_Estrategia_wordcloud.png",
    "3_Habilidades_wordcloud.png",
    "3_Herramienta de Evaluación_wordcloud.png",
    "3_wordcloud_general.png",
    "3_Medio_wordcloud.png",
    "3_Nivel de Escolaridad_wordcloud.png",
    "3_Propiedades Psicométricas_wordcloud.png",
    "3_wordcloud_general.png",
]

network_image = "3_co_word_network.png"

# Mostrar gráficos de barras
st.subheader("Gráficos de Barras de Frecuencia")
for img in bar_images:
    path = os.path.join(image_folder, img)
    if os.path.exists(path):
        st.image(path, caption=img.replace("_", " ").replace(".png", ""), use_column_width=True)
    else:
        st.warning(f"No se encontró la imagen: {img}")

# Mostrar nubes de palabras
st.subheader("Nubes de Palabras")
for img in wordcloud_images:
    path = os.path.join(image_folder, img)
    if os.path.exists(path):
        st.image(path, caption=img.replace("_", " ").replace(".png", ""), use_column_width=True)
    else:
        st.warning(f"No se encontró la imagen: {img}")

# Mostrar red de co-ocurrencia
st.subheader("Red de Co-ocurrencia (Co-Word Network)")
network_path = os.path.join(image_folder, network_image)
if os.path.exists(network_path):
    st.image(network_path, caption="Co-Word Network", use_column_width=True)
else:
    st.warning("No se encontró la imagen de co-word network.")

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
