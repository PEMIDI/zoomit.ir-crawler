from peewee import MySQLDatabase, Model, DateTimeField
from src.config import SQL_USERNAME, SQL_PASSWORD, SQL_HOST, SQL_PORT
from datetime import datetime


database = MySQLDatabase('zoomit', user=SQL_USERNAME, password=SQL_PASSWORD,
                         host=SQL_HOST, port=SQL_PORT)


class BaseModel(Model):
    created_time = DateTimeField(default=datetime.now())

    class Meta:
        database = database
