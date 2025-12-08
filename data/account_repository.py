import json
from models.account import Account

class AccountRepository:
    def __init__(self):
        self.file_path = "storage/accounts.json"
    
    def read_accounts_from_file(self) -> list[dict]:
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return data


    def write_accounts_to_file(self, accounts: list[dict]) -> None:
        with open(self.file_path, "w") as file:
            json.dump(accounts, file, indent=4)
    

    def dict_to_account(self, account_dict: dict) -> Account:
        return Account(
            account_id=account_dict["account_id"],
            owner_id=account_dict["owner_id"],
            balance=account_dict["balance"]
        )

    def account_to_dict(self, account: Account) -> dict:
        return {
            "account_id": account.account_id,
            "owner_id": account.owner_id,
            "balance": account.balance
        }

