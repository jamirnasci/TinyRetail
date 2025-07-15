from peewee import Model, AutoField, CharField, DecimalField, IntegerField, ForeignKeyField
from models.base import BaseModel
from models.sale_list import SaleList

class Sale(BaseModel):
    id = AutoField()
    total = DecimalField(null = False)
    total_itens = IntegerField(null = False)
    sale_list = ForeignKeyField(SaleList)