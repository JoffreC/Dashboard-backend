from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer

from apps.dashboards.domain.entities.year_contribution import YearContribution


class YearContributionSerializer(DocumentSerializer):
    class Meta:
        model = YearContribution
        fields = ['year', 'num_articles']

    # year = serializers.IntegerField()
    # num_articles = serializers.IntegerField()

    