from abc import ABC, abstractmethod


class ArticleRepository(ABC):
    @abstractmethod
    def get_total(self) -> object:
        pass
