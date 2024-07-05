from apps.dashboards.application.services.general_dashboard_service import GeneralDashboardService


class SummaryUseCase:
    def __init__(self, general_service:GeneralDashboardService):
        self.general_service = general_service

    def execute(self):
        return self.general_service.get_summary_info()
