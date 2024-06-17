from mongoengine import Document, fields, EmbeddedDocument

from apps.dashboards.domain.entities.topic import Topic
from apps.dashboards.domain.entities.year_contribution import YearContribution


class Province(Document):
    name = fields.StringField()
    years = fields.EmbeddedDocumentListField(YearContribution)
    topics = fields.EmbeddedDocumentListField(Topic)
    num_articles = fields.IntField()
