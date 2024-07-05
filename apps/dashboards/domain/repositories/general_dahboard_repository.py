from abc import ABC, abstractmethod


class GeneralDashboardRepository(ABC):
    @abstractmethod
    def get_dashboard_info(self):
        pass

    @abstractmethod
    def get_line_info(self):
        pass

    @abstractmethod
    def get_bar_info(self):
        pass

    @abstractmethod
    def get_tree_info(self):
        pass

    # @abstractmethod
    # def get_last_years(self):
    #     pass
    #
    # @abstractmethod
    # def get_top_topics(self):
    #     pass
    #
    # @abstractmethod
    # def get_top_affiliations(self):
    #     pass
    #
    # @abstractmethod
    # def get_authors_info(self):
    #     pass
    #
    # @abstractmethod
    # def get_affiliations_info(self):
    #     pass
    #
    # @abstractmethod
    # def get_articles_topics_info(self):
    #     pass