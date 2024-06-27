from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer

from apps.dashboards.domain.entities.affiliation import Affiliation
from apps.dashboards.infrastructure.api.v1.serializers.topic_serializer import TopicSerializer
from apps.dashboards.infrastructure.api.v1.serializers.year_contribution_serializer import YearContributionSerializer


class AffiliationSerializer(DocumentSerializer):
    years = YearContributionSerializer(many=True)
    topics = TopicSerializer(many=True)

    class Meta:
        model = Affiliation
        fields = ['id_affiliation', 'name', 'years', 'topics', 'total_articles']

    # id_affiliation = serializers.CharField()
    # name = serializers.CharField()
    # years = YearContributionSerializer(many=True)
    # topics = TopicSerializer(many=True)
    # total_articles = serializers.IntegerField()
