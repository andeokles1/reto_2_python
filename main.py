import datetime
from db.migrations import create_db
from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from controllers.charge_controller import ChargeController
from controllers.payment_controller import PaymentController


# User Creation
def create_user():
    print("Please input the next fields to create a new user.")
    name = input("Name: ")
    age = int(input("Age: "))
    try:
        user = UserController.create_user(name=name, age=age)
        print("User has been created correctly")
        account_limit = int(input("Account limit: "))
        AccountController.create_account(user=user,
                                         balance=0,
                                         open_date=datetime.datetime.now(),
                                         limit=account_limit)
    except ValueError:
        print("User could not be created!")


# Search for a user
def search_user():
    name = input("Please input the user name to search: ")
    try:
        user = UserController.get_user_by_name(name=name)
        if user is not None:
            print("The following user was found:")
            print("ID: ", user.id)
            print("Name: ", user.name)
            print("Age: ", user.age)
            account = AccountController.get_account_by_user(user=user)
            if account is not None:
                print("The following account is linked to the user:")
                print("Balance: ", account.balance)
                print("Open date: ", account.open_date)
                print("Limit: ", account.limit)
                card = CardController.get_card_by_account(account=account)
                if card:
                    print("The following card is linked to the account:")
                    print("Name: ", card.name)
        else:
            print("Couldn't find an user with that name")
    except ValueError:
        print("User could not be found!")


# Update User Name
def update_user():
    name = input("Please input the user name to be updated: ")
    try:
        user = UserController.get_user_by_name(name=name)
        if user is not None:
            print("The user has been found!")
            new_name = input(f"Current name: {user.name} | Please input new name: ")
            new_age = int(input(f"Current age: {user.age} | Please input new age: "))
            try:
                UserController.update_name(user=user, name=new_name)
                UserController.update_age(user=user, age=new_age)
            except ValueError:
                print("Couldn't update user!")
        else:
            print("Couldn't find an user with that name!")

    except ValueError:
        print("User could not be updated!")


# Delete User
def delete_user():
    name = input("Please input the user name to delete: ")
    try:
        user = UserController.get_user_by_name(name=name)
        if user is not None:
            try:
                UserController.delete_user(user=user)
                print('The user has been deleted')
            except ValueError:
                print("Couldn't delete user!")
        else:
            print("Couldn't find an user with that name!")

    except ValueError:
        print("User could not be deleted!")


# Add Card
def add_card():
    user_name = input("Input your User Name: ")
    try:
        user = UserController.get_user_by_name(name=user_name)
        if user is not None:
            user_account = AccountController.get_account_by_user(user=user)
            if user_account is not None:
                name = input("Number: ")
                cvv = input("CVV: ")
                new_card = CardController.create_card(account=user_account, name=name, cvv=cvv)
                print(new_card.name)
                print("Card has been created successfully")
            else:
                print("Couldn't find an account for the user")
        else:
            print("Couldn't find an user with that name!")
    except ValueError:
        print("User could not be created!")


def search_card():
    user_name = input("Please input the card's user name: ")
    try:
        user = UserController.get_user_by_name(name=user_name)
        if user is not None:
            user_account = AccountController.get_account_by_user(user=user)
            if user_account is not None:
                card = CardController.get_card_by_account(account=user_account)
                if card:
                    print("Card linked to the account:")
                    print("Number: ", card.name)
                else:
                    print("Couldn't find a card for that account")
            else:
                print("Couldn't find an account for the user")
        else:
            print("Couldn't find an user with that name!")

    except ValueError:
        print("User could not be created!")


def update_card():
    card_user_name = input("Please input the card's user name: ")
    try:
        user = UserController.get_user_by_name(name=card_user_name)
        if user is not None:
            user_account = AccountController.get_account_by_user(user=user)
            if user_account is not None:
                card = CardController.get_card_by_account(account=user_account)
                if card:
                    print("The following card has been found")
                    print("Number: ", card.name)
                    new_number = input("Enter your new number: ")
                    old_cvv = input("Enter you actual cvv: ")
                    if old_cvv == card.cvv:
                        new_cvv = input("Enter your new cvv")
                        CardController.update_card(card, new_number, new_cvv)
                        print("Card updated successfully")
                    else:
                        print("Sorry, CVV entered doesn't match")
                else:
                    print("Couldn't find a card for that account")
            else:
                print("Couldn't find an account for the user")
        else:
            print("Couldn't find an user with that name!")

    except ValueError:
        print("User could not be created!")


def delete_card():
    user_name = input("Please input the user of the card you want to delete: ")
    try:
        user = UserController.get_user_by_name(name=user_name)
        if user is not None:
            user_account = AccountController.get_account_by_user(user=user)
            if user_account is not None:
                card = CardController.get_card_by_account(account=user_account)
                if card:
                    CardController.delete_card(card=card)
                    print("Card deleted successfully")
                else:
                    print("Couldn't find a card for that account")
            else:
                print("Couldn't find an account for the user")
        else:
            print("Couldn't find an user with that name!")

    except ValueError:
        print("User could not be deleted!")


def make_charge():
    print("You're about to make a charge, please input the user name to proceed.")
    name = input("Name: ")
    try:
        user = UserController.get_user_by_name(name=name)
        if user is not None:
            account = AccountController.get_account_by_user(user=user)
            if account is not None:
                card = CardController.get_card_by_account(account=account)
                print("-- Card found --")
                print("Number: ", card.name)
                amount = float(input("Please select the amount to charge:"))
                input_cvv = input("Please confirm your CVV:")
                if input_cvv == card.cvv:
                    ChargeController.receive_charge(card=card, date_time=datetime.datetime.now(), amount=amount)
                    print("Charge added")
                else:
                    print("Sorry, CVV entered doesn't match")
        else:
            print("This user doesn't exist!")

    except RuntimeError:
        print("An unexpected error has occurred!")


def make_payment():
    name = input("Input your name: ")
    try:
        user = UserController.get_user_by_name(name=name)
        if user is not None:
            account = AccountController.get_account_by_user(user=user)
            if account is not None:
                print("¡An account has been found!")
                print("Balance: ", account.balance)
                print("Open date: ", account.open_date)
                print("Limit: ", account.limit)
                amount = float(input("Payment amount: "))
                if AccountController.update_balance(account=account, amount=amount):
                    PaymentController.make_payment(account=account, date_time=datetime.datetime.now(), amount=amount)
                    print("Payment successful!")

                else:
                    print("An error has occurred processing your payment. Please verify your balance and limit")
        else:
            print("This user doesn't exist, please verify the name is correct")

    except RuntimeError:
        print("An unexpected error has occurred!")


def update_account_limit():
    name = input("Input the name of the owner of the account for the limit to be changed: ")
    try:
        user = UserController.get_user_by_name(name=name)
        if user is not None:
            account = AccountController.get_account_by_user(user=user)
            if account is not None:
                print("¡An account has been found!")
                print("Balance: ", account.balance)
                print("Open date: ", account.open_date)
                print("Limit: ", account.limit)
                new_limit = float(input("New limit: "))
                if account.balance > new_limit:
                    print("The current balance of the account must not exceed the new limit!")
                elif AccountController.update_limit(account=account, limit=new_limit):
                    print("The limit has been updated!")
                else:
                    print("There has been an error")
        else:
            print("Not possible to find the username, please try again.")

    except RuntimeError:
        print("An unexpected error has occurred!")


# Menus
def bank_menu():
    while True:
        print('')
        print('**************************Bank Application - Challenge #2 Thincrs*********************\n')
        print('1-. Manage Users')
        print('2-. Manage Cards')
        print('3-. Make a Charge')
        print('4-. Make a payment')
        print('5-. Exit \n')

        choice = int(input('Please enter an option: '))
        if (choice == 1):
            users_menu()
        if (choice == 2):
            cards_menu()
        if (choice == 3):
            make_charge()
        if (choice == 4):
            make_payment()
        if (choice == 5):
            print("Exiting...")
            break


def users_menu():
    while True:
        print('')
        print('**************************Users Menu*********************\n')
        print('1-. Create User')
        print('2-. Search for a user')
        print('3-. Update User')
        print('4-. Delete User')
        print('5-. Return to Main Menu \n')

        choice = int(input('Please enter an option: '))
        if choice == 1:
            create_user()
        if choice == 2:
            search_user()
        if choice == 3:
            update_user()
        if choice == 4:
            delete_user()
        if choice == 5:
            return


def cards_menu():
    while True:
        print('')
        print('**************************Cards Menu*********************\n')
        print('1-. Add Cards')
        print('2-. Search for a Card')
        print('3-. Update Card')
        print('4-. Delete Card')
        print('5-. Return to Main Menu \n')

        choice = int(input('Please enter an option: '))
        if choice == 1:
            add_card()
        if choice == 2:
            search_card()
        if choice == 3:
            update_card()
        if choice == 4:
            delete_card()
        if choice == 5:
            return


if __name__ == "__main__":
    create_db('./db/db_oltp.db')
    bank_menu()
