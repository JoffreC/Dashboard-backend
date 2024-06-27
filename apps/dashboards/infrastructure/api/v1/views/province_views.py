from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.dashboards.application.services.affiliation_service import AffiliationService
from apps.dashboards.application.services.province_service import ProvinceService
from apps.dashboards.application.use_cases.affiliation_use_case import AffiliationUseCase
from apps.dashboards.application.use_cases.all_provinces_use_case import AllProvinceUseCase
from apps.dashboards.application.use_cases.province_use_case import ProvinceUseCase
from apps.dashboards.domain.entities.province import Province
from apps.dashboards.infrastructure.api.v1.serializers.province_serializer import ProvinceSerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    province_service = ProvinceService()

    def retrieve(self, request, *args, **kwargs):
        province_id = request.query_params.get('id_province')
        province_use_case = ProvinceUseCase(province_service=self.province_service)
        province = province_use_case.execute(id_province=province_id)
        serializer = self.get_serializer(province, many=False)
        data = serializer.data
        return Response({'Province': data})

    def list(self, request, *args, **kwargs):
        all_province_use_case = AllProvinceUseCase(province_service=self.province_service)
        provinces = all_province_use_case.execute()
        serializer = self.get_serializer(provinces, many=True)
        data = serializer.data
        return Response({'Provinces': data})
