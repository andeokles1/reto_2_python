from peewee import *

db = SqliteDatabase('./db/db_oltp.db', timeout=10)


class User(Model):
    name = CharField()
    age = IntegerField()


    class Meta:
        database = db
