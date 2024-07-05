from neomodel import db

from apps.dashboards.domain.entities.affiliation import Affiliation
from apps.dashboards.domain.entities.author import Author
from apps.dashboards.domain.entities.country import Country
from apps.dashboards.domain.entities.province import Province
from apps.dashboards.domain.entities.topic import Topic
from apps.dashboards.domain.entities.year_contribution import YearContribution
from apps.dashboards.domain.repositories.update_repository import UpdateRepository
from apps.dashboards.utils.utils import extract_year, count_articles_per_year, count_articles_per_year_author, \
    process_city, find_province, process_affiliation_name, count_province, count_articles_per_year_country


class UpdateService(UpdateRepository):
    def update_affiliation(self):
        query = """
                MATCH (ar:Article)-[b:BELONGS_TO]->(af:Affiliation)
                OPTIONAL MATCH (ar)-[u:USES]->(t:Topic)
                RETURN af.scopus_id, af.name, ar.scopus_id, ar.publication_date, t.name
            """
        results, meta = db.cypher_query(query)

        af_scopus_ids = []
        af_names = []
        ar_scopus_ids = []
        ar_publication_dates = []
        topics = []

        for result in results:
            af_scopus_ids.append(result[0])
            af_names.append(result[1])
            ar_scopus_ids.append(result[2])
            ar_publication_dates.append(result[3])
            topics.append(result[4] if result[4] is not None else " ")

        years = extract_year(ar_publication_dates)

        affiliations_data = count_articles_per_year(af_scopus_ids, af_names, ar_scopus_ids, years, topics)

        for affiliation_data in affiliations_data:
            # Crear YearContribution objects para años
            years = [YearContribution(year=year_info['year'], num_articles=year_info['numArticles']) for year_info in
                     affiliation_data['years']]

            # Crear Topic objects
            topics = []
            for topic_data in affiliation_data['topics']:
                num_articles_per_year = [YearContribution(year=year_info['year'], num_articles=year_info['numArticles'])
                                         for year_info in topic_data['topic_years']]
                topic = Topic(topic_name=topic_data['topic'], num_articles_per_year=num_articles_per_year,
                              total_topic_articles=topic_data['totalTopicArticles'])
                topics.append(topic)

            # Crear Affiliation object
            affiliation = Affiliation(
                id_affiliation=affiliation_data['idScopus'],
                name=affiliation_data['name'],  # Asegurarse de incluir el nombre
                years=years,
                topics=topics,
                total_articles=affiliation_data['totalArticles']
            )
            affiliation.save()

    def update_province(self):
        query = """
            MATCH (ar:Article)-[b:BELONGS_TO]->(af:Affiliation)
            OPTIONAL MATCH (ar)-[u:USES]->(t:Topic)
            RETURN af.scopus_id, af.name, af.city, ar.scopus_id, ar.publication_date, t.name
            """
        results, meta = db.cypher_query(query)

        af_scopus_ids = []
        af_names = []
        af_cities = []
        ar_scopus_ids = []
        ar_publication_dates = []
        topics = []

        for result in results:
            af_scopus_ids.append(result[0])
            af_names.append(result[1])
            af_cities.append(result[2])
            ar_scopus_ids.append(result[3])
            ar_publication_dates.append(result[4])
            topics.append(result[5] if result[5] is not None else " ")

        years = extract_year(ar_publication_dates)
        provinces = process_affiliation_name(af_cities, ar_scopus_ids, years, topics)
        provinces_data = count_province(provinces)

        for province_data in provinces_data:
            years = [YearContribution(year=year_info['year'], num_articles=year_info['numArticles']) for year_info in
                     province_data['years']]
            topics = []
            for topic_data in province_data['topics']:
                num_articles_per_year = [YearContribution(year=year_info['year'], num_articles=year_info['numArticles'])
                                         for year_info in topic_data['topic_years']]
                topic = Topic(topic_name=topic_data['topic'], num_articles_per_year=num_articles_per_year,
                              total_topic_articles=topic_data['totalTopicArticles'])
                topics.append(topic)

            province = Province(
                id_province=province_data["id_provincia"],
                name=province_data["provincia"],
                years=years,
                topics=topics,
                num_articles=province_data["num_articles"],
            )
            province.save()

    def update_author(self):
        query = """
                MATCH (au:Author)-[w:WROTE]->(ar:Article)
                OPTIONAL MATCH (ar)-[u:USES]->(t:Topic)
                RETURN au.scopus_id, ar.scopus_id, ar.publication_date, t.name
                """
        results, meta = db.cypher_query(query)

        au_scopus_ids = []
        ar_scopus_ids = []
        ar_publication_dates = []
        topics = []

        for result in results:
            au_scopus_ids.append(result[0])
            ar_scopus_ids.append(result[1])
            ar_publication_dates.append(result[2])
            topics.append(result[3] if result[3] is not None else " ")

        years = extract_year(ar_publication_dates)

        authors_data = count_articles_per_year_author(au_scopus_ids, ar_scopus_ids, years, topics)

        for author_data in authors_data:
            # Crear YearContribution objects para años
            years = [YearContribution(year=year_info['year'], num_articles=year_info['numArticles']) for year_info in
                     author_data['years']]

            # Crear Topic objects
            topics = []
            for topic_data in author_data['topics']:
                num_articles_per_year = [YearContribution(year=year_info['year'], num_articles=year_info['numArticles'])
                                         for year_info in topic_data['topic_years']]
                topic = Topic(topic_name=topic_data['topic'], num_articles_per_year=num_articles_per_year,
                              total_topic_articles=topic_data['totalTopicArticles'])
                topics.append(topic)

            # Crear Author object
            author = Author(
                scopus_id=author_data['idScopus'],
                years=years,
                topics=topics,
                total_articles=author_data['totalArticles']
            )
            author.save()

    def update_country(self):
        query = """
                MATCH (ar:Article)
                OPTIONAL MATCH (ar)-[u:USES]->(t:Topic)
                RETURN ar.scopus_id, ar.publication_date, t.name
                """
        results, meta = db.cypher_query(query)

        ar_scopus_ids = []
        ar_publication_dates = []
        topics = []

        for result in results:
            ar_scopus_ids.append(result[0])
            ar_publication_dates.append(result[1])
            topics.append(result[2] if result[2] is not None else " ")

        years = extract_year(ar_publication_dates)

        # Supongamos que count_articles_per_year_country ya está definida correctamente

        country_data_list = count_articles_per_year_country(ar_scopus_ids, years, topics)

        for country_data in country_data_list:
            # Crear YearContribution objects para años
            years_contributions = [YearContribution(year=year_info['year'], num_articles=year_info['numArticles']) for
                                   year_info in country_data['years']]

            # Crear Topic objects
            topics_list = []
            for topic_data in country_data['topics']:
                num_articles_per_year = [YearContribution(year=year_info['year'], num_articles=year_info['numArticles'])
                                         for year_info in topic_data['topic_years']]
                topic = Topic(topic_name=topic_data['topic'], num_articles_per_year=num_articles_per_year,
                              total_topic_articles=topic_data['totalTopicArticles'])
                topics_list.append(topic)

            authors = self.get_authors_count()
            affiliations = self.get_affiliations_count()
            topics = self.get_topics_count()

            # Crear Country object
            country_obj = Country(
                name="Ecuador",
                years=years_contributions,
                topics=topics_list,
                total_authors=authors,
                total_articles=country_data['totalArticles'],
                total_affiliations=affiliations,
                total_topics=topics,
            )

            country_obj.save()

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
