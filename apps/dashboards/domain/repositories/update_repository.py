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
