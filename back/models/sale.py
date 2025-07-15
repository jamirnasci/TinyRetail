from peewee import Model, AutoField, DecimalField, IntegerField
from models.base import BaseModel

class Sale(BaseModel):
    id = AutoField()
    total = DecimalField(null = False)
    total_itens = IntegerField(null = False)