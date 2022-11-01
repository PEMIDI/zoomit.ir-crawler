from peewee import MySQLDatabase, Model, TextField, CharField,BooleanField, ForeignKeyField, DateTimeField
from config import SQL_USERNAME, SQL_PASSWORD, SQL_HOST, SQL_PORT
from datetime import datetime


database = MySQLDatabase('zoomit', user=SQL_USERNAME, password=SQL_PASSWORD,
                         host=SQL_HOST, port=SQL_PORT)


class BaseModel(Model):
    created_time = DateTimeField(default=datetime.now())

    class Meta:
        database = database


class Category(BaseModel):
    name = CharField()


class Author(BaseModel):
    name = CharField()


class Article(BaseModel):
    url = CharField(null=True)
    title = CharField(null=True)
    body = TextField(null=True)
    is_completed = BooleanField(default=False)
    category = ForeignKeyField(Category, backref='articles')
    author = ForeignKeyField(Author, backref='authors')

