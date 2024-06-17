from mongoengine import EmbeddedDocument, fields

from apps.dashboards.domain.entities.year_contribution import YearContribution


class Topic(EmbeddedDocument):
    topic_name = fields.StringField()
    num_articles_per_year = fields.EmbeddedDocumentListField(YearContribution)
