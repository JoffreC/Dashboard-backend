from collections import defaultdict

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.dashboards.application.services.affiliation_service import AffiliationService
from apps.dashboards.application.use_cases.affiliation_use_case import AffiliationUseCase
from apps.dashboards.application.use_cases.all_affiliations_use_case import AllAffiliationsUseCase
from apps.dashboards.domain.entities.affiliation import Affiliation
from apps.dashboards.infrastructure.api.v1.serializers.affiliation_serializer import AffiliationSerializer


class AffiliationViewSet(viewsets.ModelViewSet):
    queryset = Affiliation.objects.all()
    serializer_class = AffiliationSerializer
    affiliation_service = AffiliationService()

    def retrieve(self, request, *args, **kwargs):
        scopus_id = request.query_params.get('scopus_id')
        affiliation_use_case = AffiliationUseCase(affiliation_service=self.affiliation_service)
        affiliation = affiliation_use_case.execute(scopus_id=scopus_id)
        serializer = self.get_serializer(affiliation, many=False)
        data = serializer.data
        return Response({'Affiliation': data})

    def list(self, request, *args, **kwargs):
        all_affiliations_use_case = AllAffiliationsUseCase(affiliation_service=self.affiliation_service)
        affiliations = all_affiliations_use_case.execute()
        serializer = self.get_serializer(affiliations, many=True)
        data = serializer.data
        return Response({'Affiliations': data})

    @action(detail=False, methods=['get'])
    def get_top_affiliations(self, request):
        affiliation_use_case = AllAffiliationsUseCase(affiliation_service=self.affiliation_service)
        affiliations = affiliation_use_case.execute()

        # Ordenar las afiliaciones por total_articles en orden descendente y obtener las primeras 20
        top_affiliations = sorted(affiliations, key=lambda x: x.total_articles, reverse=True)[:20]

        # Formatear la primera parte de la respuesta
        bar_frequency = [
            {
                "name": affiliation.name,
                "value": affiliation.total_articles
            }
            for affiliation in top_affiliations
        ]

        # Formatear la segunda parte de la respuesta
        series_data = defaultdict(list)
        for affiliation in top_affiliations:
            for year_contribution in affiliation.years:
                series_data[affiliation.name].append({
                    "name": str(year_contribution.year),
                    "value": year_contribution.num_articles
                })

        series_response = [
            {
                "name": affiliation_name,
                "series": series
            }
            for affiliation_name, series in series_data.items()
        ]

        response_data = {
            "Bar": {"frequency": bar_frequency},
            "Affiliations": series_response
        }

        return Response(response_data)