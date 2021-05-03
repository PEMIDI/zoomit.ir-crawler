from models.base_db import BaseModel


class Category(BaseModel):
    name = CharField()
    url = CharField()

