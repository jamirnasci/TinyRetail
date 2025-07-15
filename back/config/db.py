from peewee import MySQLDatabase

db = MySQLDatabase(
    'tinyretail',  # <- nome do banco como primeiro argumento
    user='root',
    password='123456',
    host='localhost',
    port=3306
)
