from apps.dashboards.domain.entities.country import Country
from apps.dashboards.domain.entities.province import Province
from apps.dashboards.domain.repositories.country_repository import CountryRepository


class CountryService(CountryRepository):

    def get_country(self):
        return Country.objects.get()

    # def get_years(self):
    #     years = Country.objects.get().years
    #     return years
    #
    # def get_topics(self):
    #
    #     return topics
    #
    # def get_totals(self):
    #     return Country.objects().only('total_authors', 'total_articles', 'total_affiliations', 'total_topics').first()