from apps.dashboards.application.services.general_dashboard_service import GeneralDashboardService


class TopTopicsUseCase:
    def __init__(self, general_service:GeneralDashboardService):
        self.general_service = general_service

    def execute(self):
        return self.general_service.get_tree_info()
