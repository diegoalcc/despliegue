import os
import json
import matplotlib.pyplot as plt
import collections

#############################################
# CARGAR ARCHIVO JSON
#############################################

def load_data(json_filepath):
    """Carga los artículos desde el archivo JSON y limita a los primeros 1000."""
    with open(json_filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data[:1000]  # Tomar solo los primeros 1000 artículos

#############################################
# FUNCIÓN PARA CONTAR FRECUENCIAS DE VARIABLES
#############################################

def count_frequencies(data, key, top_n=15):
    """Cuenta cuántas veces aparece cada valor en la clave especificada."""
    counter = collections.Counter([item.get(key, "Unknown").split(",")[0] for item in data])  # Tomar el primer autor
    return counter.most_common(top_n)  # Obtener los N valores más frecuentes

#############################################
# FUNCIÓN PARA AGRUPAR POR AÑO Y TIPO DE PRODUCTO
#############################################

def group_by_year_and_type(data):
    """Agrupa los productos por año y tipo de publicación."""
    grouped_data = collections.defaultdict(lambda: collections.Counter())

    for item in data:
        year = item.get("year", "Unknown")
        product_type = item.get("type", "Unknown")
        grouped_data[year][product_type] += 1

    return grouped_data

#############################################
# FUNCIÓN PARA GENERAR GRÁFICOS
#############################################

def plot_bar_chart(data, title, xlabel, ylabel, filename):
    """Genera un gráfico de barras y lo guarda."""
    labels, values = zip(*data)

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

def plot_yearly_trends(grouped_data, filename):
    """Genera un gráfico de líneas que muestra la tendencia por año y tipo de producto."""
    plt.figure(figsize=(12, 6))

    # Filtrar años entre 2010 y 2025
    years = [year for year in sorted(grouped_data.keys()) if year.isdigit() and 2010 <= int(year) <= 2025]

    for product_type in {"article", "conference", "book", "chapter"}:
        counts = [grouped_data[year][product_type] for year in years]
        plt.plot(years, counts, marker='o', label=product_type)

    plt.xlabel("Año de publicación")
    plt.ylabel("Cantidad de productos")
    plt.title("Distribución de productos por año (2010-2025)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Gráfico guardado: {filename}")
    plt.close()

#############################################
# EJECUCIÓN DEL SCRIPT
#############################################

def main():
    """Procesa los datos y genera los gráficos solicitados."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_filepath = os.path.join(script_dir, "processed_articles.json")

    if not os.path.exists(json_filepath):
        print("No se encontró el archivo JSON.")
        return
    
    results_folder = os.path.join(script_dir, "resultados")
    os.makedirs(results_folder, exist_ok=True)

    # Cargar los datos (solo los primeros 1000 artículos)
    data = load_data(json_filepath)

    # Generar estadísticas
    top_authors = count_frequencies(data, "author")
    top_journals = count_frequencies(data, "journal")
    top_publishers = count_frequencies(data, "publisher")
    yearly_product_data = group_by_year_and_type(data)

    # Guardar gráficos con prefijo "2_"
    plot_bar_chart(top_authors, "Top 15 Autores con Más Publicaciones", "Cantidad de Publicaciones", "Autores", os.path.join(results_folder, "2_top_authors.png"))
    plot_bar_chart(top_journals, "Top 15 Journals con Más Publicaciones", "Cantidad de Publicaciones", "Journals", os.path.join(results_folder, "2_top_journals.png"))
    plot_bar_chart(top_publishers, "Top 15 Publishers con Más Publicaciones", "Cantidad de Publicaciones", "Publishers", os.path.join(results_folder, "2_top_publishers.png"))
    plot_yearly_trends(yearly_product_data, os.path.join(results_folder, "2_yearly_trends.png"))

    print("Proceso completado: estadísticas generadas y gráficos guardados.")

if __name__ == "__main__":
    main()
