from models import database, Article, Category, Author


def create_table():
    database.create_tables([Article, Category, Author], safe=True)

