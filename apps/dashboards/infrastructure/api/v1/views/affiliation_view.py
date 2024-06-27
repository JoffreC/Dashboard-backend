from rest_framework import viewsets
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

