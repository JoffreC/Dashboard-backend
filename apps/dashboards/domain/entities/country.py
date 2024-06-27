from mongoengine import Document, fields

from apps.dashboards.domain.entities.topic import Topic
from apps.dashboards.domain.entities.year_contribution import YearContribution


class Country(Document):
    years = fields.EmbeddedDocumentListField(YearContribution)
    topics = fields.EmbeddedDocumentListField(Topic)
    num_articles = fields.IntField()
