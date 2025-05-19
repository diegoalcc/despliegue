import os
import json
import matplotlib.pyplot as plt
import collections

def load_data(json_filepath):
    with open(json_filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data[:1000]

def count_frequencies(data, key, top_n=15):
    counter = collections.Counter([item.get(key, "Unknown").split(",")[0] for item in data])
    return counter.most_common(top_n)

def group_by_year_and_type(data):
    grouped_data = collections.defaultdict(lambda: collections.Counter())
    for item in data:
        year = item.get("year", "Unknown")
        product_type = item.get("type", "Unknown")
        grouped_data[year][product_type] += 1
    return grouped_data

def plot_bar_chart(data, title, xlabel, ylabel, filename):
    labels, values = zip(*data)
    plt.figure(figsize=(12, 6))
    plt.barh(labels, values, color="skyblue")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title, fontsize=14)
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def plot_yearly_trends(grouped_data, filename):
    plt.figure(figsize=(12, 6))
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
    plt.close()

def estadisticas_generales(json_filepath="processed_articles.json"):
    if not os.path.exists(json_filepath):
        print(f"Archivo no encontrado: {json_filepath}")
        return

    data = load_data(json_filepath)
    top_authors = count_frequencies(data, "author")
    top_journals = count_frequencies(data, "journal")
    top_publishers = count_frequencies(data, "publisher")
    yearly_product_data = group_by_year_and_type(data)

    results_folder = os.path.join(os.path.dirname(json_filepath), "resultados")
    os.makedirs(results_folder, exist_ok=True)

    plot_bar_chart(top_authors, "Top 15 Autores con Más Publicaciones", "Cantidad de Publicaciones", "Autores", os.path.join(results_folder, "2_top_authors.png"))
    plot_bar_chart(top_journals, "Top 15 Journals con Más Publicaciones", "Cantidad de Publicaciones", "Journals", os.path.join(results_folder, "2_top_journals.png"))
    plot_bar_chart(top_publishers, "Top 15 Publishers con Más Publicaciones", "Cantidad de Publicaciones", "Publishers", os.path.join(results_folder, "2_top_publishers.png"))
    plot_yearly_trends(yearly_product_data, os.path.join(results_folder, "2_yearly_trends.png"))
