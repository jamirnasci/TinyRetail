from peewee import Model, AutoField, CharField
from models.base import BaseModel

class User(BaseModel):
    id = AutoField()
    name = CharField(null = False)
    email = CharField(null = False)
    phone = CharField(null = False)
    password = CharField(null = False)