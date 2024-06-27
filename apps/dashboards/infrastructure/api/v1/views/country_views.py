from rest_framework import viewsets
from rest_framework.response import Response

from apps.dashboards.application.services.country_service import CountryService
from apps.dashboards.application.use_cases.country_topics_use_case import CountryTopicsUseCase
from apps.dashboards.application.use_cases.country_years_use_case import CountryYearsUseCase
from apps.dashboards.infrastructure.api.v1.serializers.topic_serializer import TopicSerializer
from apps.dashboards.infrastructure.api.v1.serializers.year_contribution_serializer import YearContributionSerializer


class CountryViewsSet(viewsets.ModelViewSet):
    country_service = CountryService()

    def retrieve(self, request, *args, **kwargs):
        country_years_use_case = CountryYearsUseCase(country_service=self.country_service)
        country_years = country_years_use_case.execute()
        serializer = YearContributionSerializer(country_years, many=True)
        data = serializer.data
        return Response({'Country-years': data})

    def list(self, request, *args, **kwargs):
        country_topics_use_case = CountryTopicsUseCase(country_service=self.country_service)
        country_topics = country_topics_use_case.execute()
        serializer = TopicSerializer(country_topics, many=True)
        data = serializer.data
        return Response({'Country-topics': data})
