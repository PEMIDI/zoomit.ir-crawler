from src.models import BaseModel
from peewee import CharField

class Category(BaseModel):
    name = CharField()
    url = CharField()

