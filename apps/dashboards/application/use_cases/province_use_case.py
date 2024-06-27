from apps.dashboards.application.services.province_service import ProvinceService


class ProvinceUseCase:
    def __init__(self, province_service: ProvinceService):
        self.province_service = province_service

    def execute(self, id_province):
        return self.province_service.get_by_id(id_province)
