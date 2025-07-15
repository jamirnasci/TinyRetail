from peewee import Model, AutoField, CharField
from models.base import BaseModel
from models.user import User

class Supplier(BaseModel):
    id = AutoField()
    name = CharField(null = False)
    email = CharField(null = False)
    phone = CharField(null = False)
    address = CharField(null = False)