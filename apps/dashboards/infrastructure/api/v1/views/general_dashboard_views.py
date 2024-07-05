from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.dashboards.application.services.general_dashboard_service import GeneralDashboardService
from apps.dashboards.application.use_cases.general_dashboard_use_case import GeneralDashboardUseCase


class GeneralDashboardView(viewsets.ModelViewSet):
    def retrieve(self, request, *args, **kwargs):
        general_service = GeneralDashboardService()
        general_use_case = GeneralDashboardUseCase(general_service=general_service)
        response = general_use_case.execute()
        return Response(response)
