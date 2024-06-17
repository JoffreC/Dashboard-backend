from typing import List

from apps.dashboards.domain.entities.author import Author


def extract_year(years_column):
    years = []
    for date in years_column:
        year = date[:4]
        years.append(year)
    return years


def process_city(city_column):
    cities = []
    for city_name in city_column:
        if ',' in city_name:
            # Separar en partes por coma y quitar espacios en blanco
            parts = [part.strip() for part in city_name.rsplit(',', 1)]

            return parts[-1], parts[0]
        else:
            # Devolver el nombre de la ciudad tal cual si no tiene comas
            return city_name, None


# def find_province(processed_city):
#     city_name, extra_info = processed_city
#     for province_id, province_info in location_data.items():
#         provincia = province_info["provincia"]
#         for canton_id, canton_info in province_info["cantones"].items():
#             if city_name.upper() == canton_info["canton"]:
#                 return provincia
#             for parroquia_id, parroquia_name in canton_info["parroquias"].items():
#                 if city_name.upper() == parroquia_name.upper():
#                     return provincia
#     return None

# Ejemplo de uso
# for processed_city in processed_cities:
#     province = find_province(processed_city, location_data)
#     print(f"City: {processed_city[0]}, Province: {province}")