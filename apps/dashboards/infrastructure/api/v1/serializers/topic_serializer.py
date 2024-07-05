from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer

from apps.dashboards.domain.entities.topic import Topic
from apps.dashboards.infrastructure.api.v1.serializers.year_contribution_serializer import YearContributionSerializer


class TopicSerializer(DocumentSerializer):
    class Meta:
        model = Topic
        fields = ['topic_name', 'num_articles_per_year','total_topic_articles']
    # topic_name = serializers.CharField()
    # num_articles_per_year = YearContributionSerializer(many=True)
