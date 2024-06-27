from apps.dashboards.application.services.affiliation_service import AffiliationService


class AffiliationUseCase:
    def __init__(self, affiliation_service: AffiliationService):
        self.affiliation_service = affiliation_service

    def execute(self, scopus_id):
        return self.affiliation_service.get_by_id(scopus_id=scopus_id)