from mongoengine import Document, fields, EmbeddedDocument

from apps.dashboards.domain.entities.topic import Topic
from apps.dashboards.domain.entities.year_contribution import YearContribution


class Affiliation(Document):
    id_affiliation = fields.IntField()
    name = fields.StringField()
    years = fields.EmbeddedDocumentListField(YearContribution)
    topics = fields.EmbeddedDocumentListField(Topic)
    total_articles = fields.IntField()

