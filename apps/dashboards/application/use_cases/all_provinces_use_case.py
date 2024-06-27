from apps.dashboards.application.services.province_service import ProvinceService


class AllProvinceUseCase:
    def __init__(self, province_service: ProvinceService):
        self.province_service = province_service

    def execute(self):
        return self.province_service.get_all()