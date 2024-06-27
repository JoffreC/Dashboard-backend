from mongoengine import fields, EmbeddedDocument


class YearContribution(EmbeddedDocument):
    year = fields.IntField()
    num_articles = fields.IntField()
