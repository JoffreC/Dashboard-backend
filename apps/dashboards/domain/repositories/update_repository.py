from abc import ABC, abstractmethod


class UpdateRepository(ABC):
    @abstractmethod
    def update_author(self):
        pass

    @abstractmethod
    def update_affiliation(self):
        pass

    @abstractmethod
    def update_province(self):
        pass

    @abstractmethod
    def update_country(self):
        pass

    @abstractmethod
    def get_authors_count(self):
        pass

    @abstractmethod
    def get_affiliations_count(self):
        pass

    @abstractmethod
    def get_articles_count(self):
        pass

    @abstractmethod
    def get_topics_count(self):
        pass
