from abc import ABC, abstractmethod


class AffiliationRepository(ABC):

    @abstractmethod
    def get_by_id(self, scopus_id) -> object:
        pass

    @abstractmethod
    def get_all(self) -> object:
        pass
