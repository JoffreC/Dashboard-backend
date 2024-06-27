from abc import ABC, abstractmethod


class CountryRepository(ABC):
    @abstractmethod
    def get_years(self):
        pass

    @abstractmethod
    def get_topics(self):
        pass
