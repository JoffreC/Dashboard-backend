from collections import defaultdict, Counter

from apps.dashboards.domain.entities.affiliation import Affiliation
from apps.dashboards.domain.entities.author import Author
from apps.dashboards.domain.entities.country import Country
from apps.dashboards.domain.repositories.general_dahboard_repository import GeneralDashboardRepository
from apps.dashboards.utils.utils import get_authors_info, get_articles_topics_info, get_affiliations_info, \
    get_last_years, get_top_topics, get_top_affiliations


class GeneralDashboardService(GeneralDashboardRepository):
    countries = Country.objects.all()

    def get_summary_info(self):
        authors = get_authors_info()
        articles_topics = get_articles_topics_info(countries=self.countries)
        affiliations = get_affiliations_info()

        data = {
            "author": authors,
            "article": articles_topics.Articles,
            "affiliation": affiliations,
            "topic": articles_topics.Topics
        }

        return data

    def get_line_info(self):
        d = get_last_years(self.countries)
        per_year = {
            "name": self.countries.name,
            "series": d.per_year
        }
        acumulative ={
            "name": self.countries.name,
            "series": d.acumulative
        }
        data = {
            "per_year": per_year,
            "acumulative": acumulative
        }
        return data

    def get_bar_info(self):
        return get_top_affiliations()

    def get_tree_info(self):
        return get_top_topics(countries=self.countries)

    # def get_dashboard_info(self):
    #     #
    #     # tree = get_top_topics(self.countries)
    #     # bar =
    #     #
    #     # response = {
    #     #     'author': authors,
    #     #     'articles_topics': articles_topics,
    #     #     'affiliations': affiliations,
    #     #     'line': line_chart,
    #     #     'bar': bar,
    #     #     'tree': tree
    #     # }
    #     return articles_topics