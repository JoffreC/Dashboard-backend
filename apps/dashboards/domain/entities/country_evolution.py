from mongoengine import Document, fields


class CountryEvolution(Document):
    year = fields.IntField()
    num_articles = fields.IntField()
