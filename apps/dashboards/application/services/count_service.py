from neomodel import db

from apps.dashboards.domain.repositories.count_repository import CountRepository


class CountService(CountRepository):
    def get_authors_count(self):
        query = """
                                MATCH (au:Author)
                                RETURN COUNT(DISTINCT au.scopus_id)
                        """
        results, meta = db.cypher_query(query)
        return results[0][0]

    def get_affiliations_count(self):
        query = """
                                MATCH (af:Affiliation)
                                RETURN COUNT(DISTINCT af.scopus_id)
                        """
        results, meta = db.cypher_query(query)

        return results[0][0]

    def get_articles_count(self):
        query = """
        Match (ar:Article)
        Return COUNT(DISTINCT ar.scopus_id)
        """

        results, meta = db.cypher_query(query)

        return results[0][0]

    def get_topics_count(self):
        query = """
                Match (t:Topic) 
                Return COUNT(t.name)
                """

        results, meta = db.cypher_query(query)

        return results[0][0]
