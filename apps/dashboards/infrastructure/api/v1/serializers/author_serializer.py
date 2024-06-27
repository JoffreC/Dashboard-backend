from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer

from apps.dashboards.domain.entities.author import Author
from apps.dashboards.infrastructure.api.v1.serializers.topic_serializer import TopicSerializer
from apps.dashboards.infrastructure.api.v1.serializers.year_contribution_serializer import YearContributionSerializer


class AuthorSerializer(DocumentSerializer):
    years = YearContributionSerializer(many=True)
    topics = TopicSerializer(many=True)

    class Meta:
        model = Author
        fields = ['scopus_id', 'years', 'topics', 'total_articles']
    # scopus_id = serializers.CharField()
    # years = YearContributionSerializer(many=True)
    # topics = TopicSerializer(many=True)
    # total_articles = serializers.IntegerField()
