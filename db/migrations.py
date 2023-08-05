import os
import time
from peewee import SqliteDatabase
from schemas.user import User
from schemas.account import Account
from schemas.card import Card
from schemas.payment import Payment
from schemas.charge import Charge


def create_db(path: str):
    if not os.path.isfile(path):
        print(f"Creating database at path: {path}")
        db = SqliteDatabase(path)
        time.sleep(1)
        db.create_tables([User, Account, Card, Charge, Payment])
        print("Database created successfully.")
        return True
