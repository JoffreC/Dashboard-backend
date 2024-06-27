from apps.dashboards.domain.entities.province import Province
from apps.dashboards.domain.repositories.province_repository import ProvinceRepository


class ProvinceService(ProvinceRepository):

    def get_by_id(self, id_province):
        province = Province.objects.get(id_province=id_province)
        return province

    def get_all(self):
        return Province.objects()
