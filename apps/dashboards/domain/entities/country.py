from mongoengine import Document, fields

from apps.dashboards.domain.entities.topic import Topic
from apps.dashboards.domain.entities.year_contribution import YearContribution


class Country(Document):
    name = fields.StringField()
    years = fields.EmbeddedDocumentListField(YearContribution)
    topics = fields.EmbeddedDocumentListField(Topic)
    total_authors = fields.IntField()
    total_articles = fields.IntField()
    total_affiliations = fields.IntField()
    total_topics = fields.IntField()
