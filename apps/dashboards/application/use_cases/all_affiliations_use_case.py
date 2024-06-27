from apps.dashboards.application.services.affiliation_service import AffiliationService


class AllAffiliationsUseCase:
    def __init__(self, affiliation_service: AffiliationService):
        self.affiliation_service = affiliation_service

    def execute(self):
        return self.affiliation_service.get_all()