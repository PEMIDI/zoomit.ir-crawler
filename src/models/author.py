from src.models import BaseModel
from peewee import CharField


class Author(BaseModel):
    name = CharField()
    