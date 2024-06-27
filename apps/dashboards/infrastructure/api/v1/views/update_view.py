from rest_framework.response import Response
from rest_framework.views import APIView

from apps.dashboards.application.services.update_service import UpdateService
from apps.dashboards.application.use_cases.update_affiliation_use_case import UpdateAffiliationUseCase
from apps.dashboards.application.use_cases.update_author_use_case import UpdateAuthorUseCase
from apps.dashboards.application.use_cases.update_country_use_case import UpdateCountryUseCase
from apps.dashboards.application.use_cases.update_province_use_case import UpdateProvinceUseCase


class UpdateView(APIView):
    update_service = UpdateService()

    def post(self, request):
        update_author_use_case = UpdateAuthorUseCase(update_service=self.update_service)
        update_author_use_case.execute()
        update_affiliation_use_case = UpdateAffiliationUseCase(update_service=self.update_service)
        update_affiliation_use_case.execute()
        update_province_use_case = UpdateProvinceUseCase(update_service=self.update_service)
        update_province_use_case.execute()
        update_country = UpdateCountryUseCase(update_service=self.update_service)
        update_country.execute()
        return Response({'message': 'mongodb updated'})

    def get(self, request):
        # Implementar la funcionalidad GET si es necesario
        return Response({'message': 'GET method is not implemented yet'})
