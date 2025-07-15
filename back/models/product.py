from peewee import Model, AutoField, CharField, DecimalField, IntegerField, ForeignKeyField
from models.base import BaseModel
from models.supplier import Supplier

class Product(BaseModel):
    id = AutoField()
    name = CharField(null = False)
    buy_price = DecimalField(null = False)
    sell_price = DecimalField(null = False)
    quantity = IntegerField(null= False)
    supplier = ForeignKeyField(Supplier)
