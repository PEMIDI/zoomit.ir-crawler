from src.models import BaseModel
from peewee import CharField, TextField, BooleanField, DateTimeField, ForeignKeyField
from src.models import Category
from src.models import Author


class Article(BaseModel):
    url = CharField(null=True)
    title = CharField(null=True)
    body = TextField(null=True)
    is_completed = BooleanField(default=False)
    posted_datetime = DateTimeField(null=True)
    category = ForeignKeyField(Category, backref='articles', null=True)
    author = ForeignKeyField(Author, backref='articles', null=True)

    
        