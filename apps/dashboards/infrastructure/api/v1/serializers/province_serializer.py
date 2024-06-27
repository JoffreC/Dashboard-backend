from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer

from apps.dashboards.domain.entities.province import Province
from apps.dashboards.infrastructure.api.v1.serializers.topic_serializer import TopicSerializer
from apps.dashboards.infrastructure.api.v1.serializers.year_contribution_serializer import YearContributionSerializer


class ProvinceSerializer(DocumentSerializer):
    years = YearContributionSerializer(many=True)
    topics = TopicSerializer(many=True)

    class Meta:
        model = Province
        fields = ['id_province', 'name', 'years', 'topics', 'num_articles']
    # id_province = serializers.CharField()
    # name = serializers.CharField()
    # years = YearContributionSerializer(many=True)
    # topics = TopicSerializer(many=True)
    # num_articles = serializers.IntegerField()


