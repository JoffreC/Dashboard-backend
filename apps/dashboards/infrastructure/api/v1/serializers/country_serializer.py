from rest_framework_mongoengine.serializers import DocumentSerializer

from apps.dashboards.domain.entities.country import Country
from apps.dashboards.infrastructure.api.v1.serializers.topic_serializer import TopicSerializer
from apps.dashboards.infrastructure.api.v1.serializers.year_contribution_serializer import YearContributionSerializer


class CountrySerializer(DocumentSerializer):
    years = YearContributionSerializer(many=True)
    topics = TopicSerializer(many=True)

    class Meta:
        model = Country
        fields = ['years', 'topics', 'num_articles']
