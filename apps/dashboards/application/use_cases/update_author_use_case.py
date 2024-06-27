from apps.dashboards.application.services.update_service import UpdateService


class UpdateAuthorUseCase:
    def __init__(self, update_service: UpdateService):
        self.update_service = update_service

    def execute(self):
        return self.update_service.update_author()
