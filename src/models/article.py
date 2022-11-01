from models.base_db import BaseModel
from peewee import CharField, TextField, BooleanField, DateTimeField, ForeignKeyField
from models.category import Category
from models.author import Author


class Article(BaseModel):
    url = CharField(null=True)
    title = CharField(null=True)
    body = TextField(null=True)
    is_completed = BooleanField(default=False)
    posted_datetime = DateTimeField(null=True)
    category = ForeignKeyField(Category, backref='articles', null=True)
    author = ForeignKeyField(Author, backref='articles', null=True)

    
        