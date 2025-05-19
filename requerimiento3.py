import os
import json
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import networkx as nx

# Cargar la definición de categorías y variables
from categorias import CATEGORIAS

#############################################
# CARGAR ARCHIVO JSON
#############################################

def load_data(json_filepath):
    """Carga los artículos desde el archivo JSON y limita a los primeros 1000."""
    with open(json_filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data[:1000]  # Tomar solo los primeros 1000 artículos

#############################################
# FUNCIÓN PARA ANALIZAR FRECUENCIA DE VARIABLES
#############################################

def analyze_category_frequencies(data):
    """Analiza la frecuencia de aparición de cada variable dentro de cada categoría en los abstracts."""
    category_counts = {category: collections.Counter() for category in CATEGORIAS}

    for item in data:
        abstract = item.get("abstract", "").lower()
        for category, variables in CATEGORIAS.items():
            for variable in variables:
                synonyms = [syn.strip().lower() for syn in variable.split("-")]
                if any(syn in abstract for syn in synonyms):
                    category_counts[category][variable] += 1

    return category_counts

#############################################
# FUNCIÓN PARA GENERAR GRÁFICO DE FRECUENCIA
#############################################

def plot_bar_chart(data, title, xlabel, ylabel, filename):
    """Genera un gráfico de barras y lo guarda."""
    labels, values = zip(*data.items())

    plt.figure(figsize=(12, 6))
    plt.barh(labels, values, color="skyblue")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title, fontsize=14)
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Gráfico guardado: {filename}")
    plt.close()

#############################################
# FUNCIÓN PARA GENERAR NUBE DE PALABRAS
#############################################

def generate_word_cloud(data, title, filename):
    """Genera una nube de palabras y la guarda."""
    word_freq = " ".join([word for word, count in data.items() for _ in range(count)])

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(word_freq)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title, fontsize=14)
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Nube de palabras guardada: {filename}")
    plt.close()

#############################################
# FUNCIÓN PARA GENERAR CO-WORD NETWORK VISUALIZATION
#############################################

def generate_co_word_network(data, filename):
    """Genera un gráfico de co-ocurrencia de palabras clave en los abstracts."""
    G = nx.Graph()

    # Agregar nodos y conexiones entre palabras que aparecen juntas
    for category, variables in CATEGORIAS.items():
        for variable in variables:
            synonyms = [syn.strip().lower() for syn in variable.split("-")]
            for i in range(len(synonyms)):
                for j in range(i + 1, len(synonyms)):
                    G.add_edge(synonyms[i], synonyms[j], weight=1)

    plt.figure(figsize=(12, 6))
    pos = nx.spring_layout(G, k=0.5)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", font_size=10)

    plt.title("Co-word Network Visualization", fontsize=14)
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Gráfico de co-word network guardado: {filename}")
    plt.close()

#############################################
# EJECUCIÓN DEL SCRIPT
#############################################

def main():
    """Procesa los datos y genera los gráficos requeridos."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_filepath = os.path.join(script_dir, "processed_articles.json")

    if not os.path.exists(json_filepath):
        print("No se encontró el archivo JSON.")
        return
    
    results_folder = os.path.join(script_dir, "resultados")
    os.makedirs(results_folder, exist_ok=True)

    # Cargar los datos
    data = load_data(json_filepath)

    # Analizar frecuencia de variables por categoría
    category_counts = analyze_category_frequencies(data)

    # Generar gráficos
    for category, counts in category_counts.items():
        plot_bar_chart(counts, f"Frecuencia de Variables en {category}", "Frecuencia", "Variables", os.path.join(results_folder, f"3_{category}_frecuencia.png"))
        generate_word_cloud(counts, f"Nube de Palabras en {category}", os.path.join(results_folder, f"3_{category}_wordcloud.png"))

    # Generar nube de palabras general
    all_words = collections.Counter()
    for counts in category_counts.values():
        all_words.update(counts)

    generate_word_cloud(all_words, "Nube de Palabras General", os.path.join(results_folder, "3_wordcloud_general.png"))

    # Generar co-word network visualization
    generate_co_word_network(category_counts, os.path.join(results_folder, "3_co_word_network.png"))

    print("Proceso completado: estadísticas generadas y gráficos guardados.")

if __name__ == "__main__":
    main()
