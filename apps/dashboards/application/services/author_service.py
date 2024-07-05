from typing import List

from neomodel import db

from apps.dashboards.domain.entities.author import Author
from apps.dashboards.domain.entities.topic import Topic
from apps.dashboards.domain.entities.year_contribution import YearContribution
from apps.dashboards.domain.repositories.author_repository import AuthorRepository


class AuthorService(AuthorRepository):

    def get_by_id(self, scopus_id):
        author = Author.objects.get(scopus_id=scopus_id)
        return author

