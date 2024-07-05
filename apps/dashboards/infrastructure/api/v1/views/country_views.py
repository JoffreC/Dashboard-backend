from collections import defaultdict

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.dashboards.application.services.country_service import CountryService
from apps.dashboards.application.use_cases.country_use_case import CountryUseCase
from apps.dashboards.domain.entities.country import Country
from apps.dashboards.infrastructure.api.v1.serializers.country_serializer import CountrySerializer


class CountryViewsSet(viewsets.ModelViewSet):
    country_service = CountryService()
    queryset = Country.objects
    serializer_class = CountrySerializer

    @action(detail=False, methods=['get'])
    def get_years(self, request):
        country_use_case = CountryUseCase(country_service=self.country_service)
        country = country_use_case.execute()

        # Filtrar los años desde 1990 hasta la actualidad
        start_year = 1990
        current_year = 2024
        filtered_years = [year for year in country.years if start_year <= year.year <= current_year]

        # Formatear los datos en la estructura requerida
        series_data = [
            {
                "name": str(yc.year),
                "value": yc.num_articles
            }
            for yc in filtered_years
        ]

        response_data = {
            "name": country.name,
            "series": series_data
        }

        return Response(response_data)
    # @action(detail=False, methods=['get'])
    # def get_years(self, request):
    #     country_use_case = CountryUseCase(country_service=self.country_service)
    #     country = country_use_case.execute()
    #     serializer = self.get_serializer(country)
    #     data = serializer.data
    #
    #     return Response({'Country-years': data.years})

    @action(detail=False, methods=['get'])
    def get_topics(self, request):
        country_use_case = CountryUseCase(country_service=self.country_service)
        country = country_use_case.execute()
        serializer = self.get_serializer(country)
        data = serializer.data
        # Ordenar los tópicos por 'total_topic_articles' en orden descendente
        sorted_topics = sorted(data['topics'], key=lambda x: x['total_topic_articles'], reverse=True)

        top_100_topics = sorted_topics[:100]

        # Filtrar los tópicos que tienen un nombre vacío
        top_100_topics = [topic for topic in top_100_topics if topic['topic_name'].strip() != ""]

        # Si la longitud de los tópicos filtrados es menor a 100, añadir más tópicos hasta llegar a 100
        if len(top_100_topics) < 100:
            additional_topics = sorted_topics[100:]
            for topic in additional_topics:
                if topic['topic_name'].strip() != "":
                    top_100_topics.append(topic)
                    if len(top_100_topics) == 100:
                        break

        response_data = [
            {
                "text": topic['topic_name'],
                "size": topic['total_topic_articles']
            }
            for topic in top_100_topics
        ]
        return Response(response_data)

    @action(detail=False, methods=['get'])
    def get_count(self, request):
        country_use_case = CountryUseCase(country_service=self.country_service)
        country = country_use_case.execute()
        serializer = self.get_serializer(country)
        data = serializer.data
        response_data = {
            "author": data['total_authors'],
            "article": data['total_articles'],
            "affiliation": data['total_affiliations'],
            "topic": data['total_topics']
        }

        return Response(response_data)

    @action(detail=False, methods=['get'])
    def get_top_topics(self, request):
        country_use_case = CountryUseCase(country_service=self.country_service)
        country = country_use_case.execute()

        # Filtrar y ordenar los topics por total_topic_articles, excluyendo aquellos con topic_name " "
        filtered_topics = [topic for topic in country.topics if topic.topic_name.strip() != ""]
        sorted_topics = sorted(filtered_topics, key=lambda x: x.total_topic_articles, reverse=True)

        # Obtener los primeros 20 topics
        top_topics = sorted_topics[:20]

        # Si el número de topics filtrados es mayor a 20, asegurar que incluimos el topic 21
        if len(sorted_topics) > 20:
            for topic in sorted_topics[20:]:
                if topic.topic_name.strip() != "":
                    top_topics.append(topic)
                    break

        # Formatear la primera parte de la respuesta
        bar_frequency = [
            {
                "name": topic.topic_name,
                "value": topic.total_topic_articles
            }
            for topic in top_topics
        ]

        # Formatear la segunda parte de la respuesta
        series_data = defaultdict(list)
        for topic in top_topics:
            for year_contribution in topic.num_articles_per_year:
                series_data[topic.topic_name].append({
                    "name": str(year_contribution.year),
                    "value": year_contribution.num_articles
                })

        series_response = [
            {
                "topic_name": topic_name,
                "series": series
            }
            for topic_name, series in series_data.items()
        ]

        response_data = {
            "Bar": {"frequency": bar_frequency},
            "Topics": series_response
        }

        return Response(response_data)