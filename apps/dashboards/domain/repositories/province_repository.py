from abc import ABC, abstractmethod


class ProvinceRepository(ABC):

    @abstractmethod
    def get_by_id(self, id) -> object:
        pass

    @abstractmethod
    def get_all(self) -> object:
        pass
