from peewee import Model
from config.db import db

class BaseModel(Model):
    class Meta:
        database = db