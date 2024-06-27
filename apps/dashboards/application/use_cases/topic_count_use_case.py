from apps.dashboards.application.services.country_service import TopicService


class TopicUseCase:
    def __init__(self, topic_service: TopicService):
        self.topic_service = topic_service

    def execute(self):
        return self.topic_service.get_total_articles()
