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
        # get raw list[dict] from user repository
        user_dicts = self.user_repo.read_users_from_file()

        # convert each dict to a user object
        users = [self.user_repo.dict_to_user(user_dict) for user_dict in user_dicts]
        # return list[User]
        return users

    def save_users(self, users: list[User]) -> None:
        # convert each user object to a dict
        user_dicts = [self.user_repo.user_to_dict(user) for user in users]

        # save dicts to file
        self.user_repo.write_users_to_file(user_dicts)

    def load_accounts(self) -> list[Account]:
        account_dicts = self.account_repo.read_accounts_from_file()
        accounts = [self.account_repo.dict_to_account(account_dict) for account_dict in account_dicts]
        return accounts

    def save_accounts(self, accounts: list[Account]) -> None:
        account_dicts = [self.account_repo.account_to_dict(account) for account in accounts]
        self.account_repo.write_accounts_to_file(account_dicts)

    def load_transactions(self) -> list[Transaction]:
        transaction_dicts = self.transaction_repo.read_transactions_from_file()
        transactions = [self.transaction_repo.dict_to_transaction(transaction_dict) for transaction_dict in transaction_dicts]
        return transactions

    def save_transactions(self, transactions: list[Transaction]) -> None:
        transaction_dicts = [self.transaction_repo.transaction_to_dict(transaction) for transaction in transactions]
        self.transaction_repo.write_transactions_to_file(transaction_dicts)


        