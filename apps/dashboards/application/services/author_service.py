from typing import List

from apps.dashboards.domain.entities.author import Author
from apps.dashboards.domain.entities.topic import Topic
from apps.dashboards.domain.entities.year_contribution import YearContribution
from apps.dashboards.domain.repositories.author_repository import AuthorRepository


class AuthorService(AuthorRepository):
    def get_articles_years_information(self, scopus_id) -> List[YearContribution]:
        author = Author.objects.get(scopus_id=scopus_id)
        years = author.years
        return years

    def get_topics_information(self, scopus_id) -> List[Topic]:
        author = Author.objects.get(scopus_id=scopus_id)
        topics = author.topics
        return topics

    def get_total_articles(self, scopus_id):
        author = Author.objects.get(scopus_id=scopus_id)
        num_articles = author.total_articles
