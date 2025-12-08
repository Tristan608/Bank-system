from data.account_repository import AccountRepository
from data.transaction_repository import TransactionRepository
from data.user_repository import UserRepository
from models.account import Account
from models.transaction import Transaction
from models.user import User


class DataLayerAPI:
    def __init__(self):
        self.user_repo = UserRepository()
        self.account_repo = AccountRepository()
        self.transaction_repo = TransactionRepository()

    def load_users(self) -> list[User]:
        pass

    def save_users(self, users: list[User]) -> None:
        pass

    def load_accounts(self) -> list[Account]:
        pass

    def save_accounts(self, accounts: list[Account]) -> None:
        pass

    def load_transactions(self) -> list[Transaction]:
        pass

    def save_transactions(self, transactions: list[Transaction]) -> None:
        pass



        