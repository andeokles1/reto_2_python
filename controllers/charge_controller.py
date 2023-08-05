from schemas.card import Card
import datetime
from schemas.charge import Charge
from schemas.account import Account
from controllers.account_controller import AccountController
from typing import Union, List


class ChargeController:
    # Create
    @staticmethod
    def receive_charge(card: Card, date_time: datetime.datetime, amount: float):
        account = Account.get(id=card.account_id)
        if amount > 0:
            card_id = card.id
            charge = Charge(card_id=card_id, date_time=date_time, amount=amount)
            AccountController.update_balance(account=account, amount=amount)
            charge.save()
            print(f'Charge successfully made to card: {card_id}')
        else:
            print('Invalid Amount')

    # Read
    @staticmethod
    def get_charge_by_id(id: int) -> Union[Charge, None]:
        try:
            return Charge.get(id=id)
        except Charge.DoesNotExist:
            print(f'Charge with id {id} does not exist')
            return None

    @staticmethod
    def get_charges_by_card(card: Card) -> Union[List, None]:
        try:
            return list(Charge.filter(card_id=card.id))
        except Card.DoesNotExist:
            print(f'No Charges were found in card with id {card.id}')
            return None

    # delete
    @staticmethod
    def delete_charge(charge: Charge):
        charge.delete_instance()
