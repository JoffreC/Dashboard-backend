from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.dashboards.application.services.author_service import AuthorService
from apps.dashboards.application.use_cases.author_use_case import AuthorUseCase
from apps.dashboards.infrastructure.api.v1.serializers.author_serializer import AuthorSerializer


class AuthorViewsSet(viewsets.ModelViewSet):
    author_service = AuthorService()
    serializer_class = AuthorSerializer

    def retrieve(self, request, *args, **kwargs):
        scopus_id = (request.query_params.get('scopus_id'))
        author_use_case = AuthorUseCase(author_service=self.author_service)
        author = author_use_case.execute(scopus_id=scopus_id)
        serializer = self.get_serializer(author)
        data = serializer.data
        return Response({'Author': data})
