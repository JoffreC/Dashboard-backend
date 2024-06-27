from apps.dashboards.domain.entities.country import Country
from apps.dashboards.domain.entities.province import Province
from apps.dashboards.domain.repositories.country_repository import CountryRepository


class CountryService(CountryRepository):
    def get_years(self):
        years = Country.objects.get().years
        return years

    def get_topics(self):
        topics = Country.objects.get().topics
        return topics
