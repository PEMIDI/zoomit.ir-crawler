from models.base_db import BaseModel
from peewee import CharField


class Author(BaseModel):
    name = CharField()
    