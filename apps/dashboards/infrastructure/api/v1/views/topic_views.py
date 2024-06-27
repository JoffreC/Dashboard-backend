from rest_framework import viewsets
from rest_framework.response import Response

from apps.dashboards.application.services.country_service import TopicService
from apps.dashboards.application.use_cases.topic_count_use_case import TopicUseCase


class TopicViewSet(viewsets.ModelViewSet):
    topic_service = TopicService()

    def retrieve(self, request, *args, **kwargs):
        total_count_use_case = TopicUseCase(topic_service=self.topic_service)
        total_count = total_count_use_case.execute()
        return Response({'Total': total_count})
