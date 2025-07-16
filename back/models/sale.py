from peewee import Model, AutoField, DecimalField, IntegerField, DateTimeField
from models.base import BaseModel
import datetime
class Sale(BaseModel):
    id = AutoField()
    total = DecimalField(null = False)
    total_itens = IntegerField(null = False)
    created_at = DateTimeField(default=datetime.datetime.now)