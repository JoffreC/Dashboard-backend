import json
from collections import defaultdict
from typing import List

from apps.dashboards.domain.entities.author import Author

with open('apps/dashboards/utils/archive/provincias.json', 'r', encoding='utf-8') as json_file:
    location_data = json.load(json_file)


def extract_year(years_column):
    years = []
    for date in years_column:
        year = date[:4]
        years.append(year)
    return years


def count_articles_per_year(af_scopus_ids, af_names, ar_scopus_ids, years, topics):
    affiliation_data = defaultdict(lambda: {
        "name": None,
        "years": defaultdict(set),  # Usamos un set para evitar duplicados
        "topics": defaultdict(lambda: defaultdict(set))
    })

    for af_scopus_id, af_name, ar_scopus_id, year, topic in zip(af_scopus_ids, af_names, ar_scopus_ids, years, topics):
        if affiliation_data[af_scopus_id]["name"] is None:
            affiliation_data[af_scopus_id]["name"] = af_name
        affiliation_data[af_scopus_id]["years"][year].add(ar_scopus_id)
        affiliation_data[af_scopus_id]["topics"][topic][year].add(ar_scopus_id)

    processed_data = []
    for af_scopus_id, data in affiliation_data.items():
        total_articles = sum(len(articles) for articles in data["years"].values())
        year_data = [{"year": year, "numArticles": len(articles)} for year, articles in data["years"].items()]

        topic_data = []
        for topic, years in data["topics"].items():
            total_topic_articles = sum(len(articles) for articles in years.values())
            topic_years_data = [{"year": year, "numArticles": len(articles)} for year, articles in years.items()]
            topic_data.append({
                "topic": topic,
                "topic_years": topic_years_data,
                "totalTopicArticles": total_topic_articles
            })

        processed_data.append({
            "idScopus": af_scopus_id,
            "name": data["name"],  # Asegurarse de incluir el nombre
            "years": year_data,
            "totalArticles": total_articles,
            "topics": topic_data
        })

    return processed_data


def count_articles_per_year_author(entity_id_column, articles_id_column, years_column, topics):
    author_data = defaultdict(lambda: {
        "years": defaultdict(set),
        "topics": defaultdict(lambda: defaultdict(int))
    })

    for entity_id, article_id, year, topic in zip(entity_id_column, articles_id_column, years_column, topics):
        author_data[entity_id]["years"][year].add(article_id)
        author_data[entity_id]["topics"][topic][year] += 1

    processed_data = []
    for entity_id, data in author_data.items():
        total_articles = sum(len(articles) for articles in data["years"].values())
        year_data = [{"year": year, "numArticles": len(articles)} for year, articles in data["years"].items()]

        topic_data = []
        for topic, years in data["topics"].items():
            total_topic_articles = sum(years.values())
            topic_years_data = [{"year": year, "numArticles": count} for year, count in years.items()]
            topic_data.append({
                "topic": topic,
                "topic_years": topic_years_data,
                "totalTopicArticles": total_topic_articles
            })

        processed_data.append({
            "idScopus": entity_id,
            "years": year_data,
            "totalArticles": total_articles,
            "topics": topic_data
        })
    return processed_data


def process_city(city_column):
    cities = []
    for city_name in city_column:
        if ',' in city_name:
            # Separar en partes por coma y quitar espacios en blanco
            parts = [part.strip() for part in city_name.rsplit(',', 1)]
            city = parts[-1], parts[0]
            cities.append(city)
        else:
            cities.append(city_name)
    provinces = []
    for processed_city in cities:
        provinces = find_province(processed_city)
    return provinces


def find_province(city_name):
    if city_name is None:
        return -1, 'Pendiente'

    city_name = city_name.upper()
    for province_id, province_info in location_data.items():
        if "provincia" in province_info:
            provincia = province_info["provincia"].upper()
            if city_name == provincia:
                return province_id, provincia
            if "cantones" in province_info:
                for canton_id, canton_info in province_info["cantones"].items():
                    if "canton" in canton_info:
                        if city_name == canton_info["canton"].upper():
                            return province_id, provincia
                    if "parroquias" in canton_info:
                        for parroquia_id, parroquia_name in canton_info["parroquias"].items():
                            if city_name == parroquia_name.upper():
                                return province_id, provincia
    return -1, 'Pendiente'


# def process_province_data(af_cities, ar_scopus_ids, ar_publication_dates, topics):
#     province_data = defaultdict(lambda: {
#         "years": defaultdict(int),  # Usamos int para contar los artículos por año
#         "topics": defaultdict(lambda: defaultdict(int))  # Usamos int para contar artículos por topic y año
#     })
#
#     for af_city, ar_scopus_id, year, topic in zip(af_cities, ar_scopus_ids, ar_publication_dates, topics):
#         if af_city is None:
#             continue
#         province_id, province_name = find_province(af_city)
#         province_data[province_id]["years"][year] += 1
#         province_data[province_id]["province_name"] = province_name
#         province_data[province_id]["topics"][topic][year] += 1
#
#     return province_data

def process_affiliation_name(af_cities, ar_scopus_ids, ar_publication_dates, topics):
    processed_data = []

    for af_city, ar_scopus_id, year, topic in zip(af_cities, ar_scopus_ids, ar_publication_dates, topics):
        if af_city is None:
            continue
        province_id, province_name = find_province(af_city)
        processed_data.append({
            "province_id": province_id,
            "province_name": province_name,
            "article_id": ar_scopus_id,
            "year": year,
            "topic": topic
        })

    return processed_data


def count_province(processed_data):
    province_data = defaultdict(lambda: {
        "years": defaultdict(int),  # Usamos int para contar los artículos por año
        "topics": defaultdict(lambda: defaultdict(int))  # Usamos int para contar artículos por topic y año
    })

    seen_combinations = set()

    for data in processed_data:
        province_id = data["province_id"]
        province_name = data["province_name"]
        article_id = data["article_id"]
        year = data["year"]
        topic = data["topic"]

        if province_id is None:
            continue

        combination = (province_id, article_id)
        if combination in seen_combinations:
            continue

        seen_combinations.add(combination)

        province_data[province_id]["years"][year] += 1
        province_data[province_id]["province_name"] = province_name
        province_data[province_id]["topics"][topic][year] += 1

    final_list = []
    for province_id, data in province_data.items():
        total_articles = sum(articles for articles in data["years"].values())
        year_data = [{"year": year, "numArticles": articles} for year, articles in data["years"].items()]

        topic_data = []
        for topic, years in data["topics"].items():
            total_topic_articles = sum(years.values())
            topic_years_data = [{"year": year, "numArticles": articles} for year, articles in years.items()]
            topic_data.append({
                "topic": topic,
                "topic_years": topic_years_data,
                "totalTopicArticles": total_topic_articles
            })

        final_list.append({
            "id_provincia": province_id,
            "provincia": province_data[province_id]["province_name"],
            "num_articles": total_articles,
            "years": year_data,
            "topics": topic_data
        })

    return final_list


from collections import defaultdict


def count_articles_per_year_country(articles_id, years, topics):
    data = {
        "years": defaultdict(set),  # Usamos set para evitar duplicados de artículos por año
        "topics": defaultdict(lambda: defaultdict(int))  # Usamos int para contar artículos por topic y año
    }

    # Llenado de datos
    for article_id, year, topic in zip(articles_id, years, topics):
        data["years"][year].add(article_id)  # Agregamos el ID del artículo al año correspondiente
        data["topics"][topic][year] += 1  # Incrementamos el conteo de artículos por tema y año

    total_articles = sum(len(articles) for articles in data["years"].values())
    year_data = [{"year": year, "numArticles": len(articles)} for year, articles in data["years"].items()]

    topic_data = []
    for topic, years in data["topics"].items():
        total_topic_articles = sum(years.values())
        topic_years_data = [{"year": year, "numArticles": count} for year, count in years.items()]
        topic_data.append({
            "topic": topic,
            "topic_years": topic_years_data,
            "totalTopicArticles": total_topic_articles
        })

    processed_data = [{
        "years": year_data,
        "totalArticles": total_articles,
        "topics": topic_data
    }]

    return processed_data
