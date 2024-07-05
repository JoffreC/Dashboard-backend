from apps.dashboards.application.services.general_dashboard_service import GeneralDashboardService


class DashboardSummaryUseCase:
    def __init__(self, dashboard_service: GeneralDashboardService):
        self.dashboard_service = dashboard_service

    def execute(self):
        return self.dashboard_service.get_summary_info()
