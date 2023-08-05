from schemas.account import Account, User
from schemas.card import Card
from typing import Union
import datetime
from controllers.account_controller import AccountController
from controllers.charge_controller import ChargeController
from controllers.payment_controller import PaymentController


class CardController:
    #Create
    @staticmethod
    def create_card(account: Account, name: str, cvv: str) -> Card:
        card = Card(account_id=account.id, name=name, cvv=cvv)
        card.save()
        return card

    #Read
    @staticmethod
    def get_card_by_id(id: int) -> Union[Card, None]:
        try:
            return Card.get(id=id)
        except Card.DoesNotExist:
            return None

    @staticmethod
    def get_card_by_account(account: Account) -> Union[Card, None]:
        try:
            return Card.get(account_id=account.id)
        except Card.DoesNotExist:
            return None

    @staticmethod
    def update_card(card: Card, name: str, cvv: str) -> bool:
        card.name = name
        card.cvv = cvv
        card.save()
        return True

    @staticmethod
    def make_a_deposit(card: Card, amount: float):
        PaymentController.make_a_payment(card, datetime.datetime.now(), amount)

    @staticmethod
    def make_a_withdrawal(card: Card, amount: float):
        ChargeController.make_a_charge(card, datetime.datetime.now(), amount)

    @staticmethod
    def get_credit_available(card: Card):
        account = Account.get(id=card.account_id)
        balance = account.balance
        if balance > 0:
            return account.limit
        else:
            return account.limit + balance

    @staticmethod
    def get_limit_credit(card: Card):
        account = Account.get(id=card.account_id)
        return account.limit

    @staticmethod
    def get_balance(card: Card):
        account = Account.get(id=card.account_id)
        return account.balance

    #Delete
    @staticmethod
    def delete_card(card: Card):
        account = Account.get(id=card.account_id)
        balance = account.balance
        if balance == 0:
            card.delete_instance()
        else:
            print('Balance must be zero to delete this card')
