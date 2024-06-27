from abc import ABC, abstractmethod


class GenericRepository(ABC):

    @abstractmethod
    def get_by_id(selfself, scopus_id) -> object:
        pass


    @abstractmethod
    def get_articles_years_information(self, scopus_id) -> object:
        pass

    @abstractmethod
    def get_topics_information(self, scopus_id) -> object:
        pass

    @abstractmethod
    def get_total_articles(self, scopus_id):
        pass
