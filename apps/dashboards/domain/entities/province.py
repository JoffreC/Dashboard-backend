from mongoengine import Document, fields, EmbeddedDocument

from apps.dashboards.domain.entities.topic import Topic
from apps.dashboards.domain.entities.year_contribution import YearContribution


class Province(Document):
    id_province = fields.IntField()
    name = fields.StringField()
    years = fields.EmbeddedDocumentListField(YearContribution)
    topics = fields.EmbeddedDocumentListField(Topic)
    num_articles = fields.IntField()