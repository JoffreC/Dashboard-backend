from mongoengine import Document, fields, EmbeddedDocument
from apps.dashboards.domain.entities.topic import Topic
from apps.dashboards.domain.entities.year_contribution import YearContribution


class Author(Document):
    scopus_id = fields.IntField()
    years = fields.EmbeddedDocumentListField(YearContribution)
    topics = fields.EmbeddedDocumentListField(Topic)
    total_articles = fields.IntField()

