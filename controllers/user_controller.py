from schemas.user import User
from schemas.account import Account
from controllers.account_controller import AccountController


class UserController:
    # Create
    @staticmethod
    def create_user(name: str, age: int) -> User:
        user = User(name=name, age=age)
        user.save()
        return user

    # Read
    @staticmethod
    def get_user_by_id(id: int) -> User:
        return User.get(id=id)

    @staticmethod
    def get_user_by_name(name: str) -> User:
        try:
            return User.get(name=name)
        except User.DoesNotExist:
            return None



    # Update

    @staticmethod
    def update_name(user: User, name: str) -> User:
        user.name = name
        user.save()
        return user

    @staticmethod
    def update_age(user: User, age: int) -> User:
        user.age = age
        user.save()
        return user

    # Delete
    @staticmethod
    def delete_user(user: User):
        try:
            account = Account.get(user_id=user.id)
        except:
            account = None
        if account is None:
            user.delete_instance()
        else:
            AccountController.delete_account(account=account)
            user.delete_instance()
