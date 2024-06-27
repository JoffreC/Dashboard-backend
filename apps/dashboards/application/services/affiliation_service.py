from apps.dashboards.domain.entities.affiliation import Affiliation
from apps.dashboards.domain.repositories.affiliation_repository import AffiliationRepository


class AffiliationService(AffiliationRepository):
    def get_by_id(self, scopus_id):
        affiliation = Affiliation.objects.get(id_affiliation=scopus_id)
        return affiliation

    def get_all(self):
        return Affiliation.objects()

