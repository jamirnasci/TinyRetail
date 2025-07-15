from peewee import Model, AutoField, CharField, IntegerField, ForeignKeyField
from models.base import BaseModel
from models.product import Product

class SaleList(BaseModel):
    id = AutoField()
    total_item = IntegerField(null = False)
    product = ForeignKeyField(Product)