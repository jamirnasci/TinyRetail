from peewee import Model, AutoField, CharField, IntegerField, ForeignKeyField
from models.base import BaseModel
from models.product import Product
from models.sale import Sale

class SaleList(BaseModel):
    id = AutoField()
    total_item = IntegerField(null = False)
    product = ForeignKeyField(Product)
    sale = ForeignKeyField(Sale, on_delete='CASCADE')