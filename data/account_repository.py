import json
import os
from json import JSONDecodeError
from models.account import Account

class AccountRepository:
    def __init__(self):
        self.file_path = "storage/accounts.json"
    
    def read_accounts_from_file(self) -> list[dict]:
        # Handle missing or empty files
        if not os.path.exists(self.file_path):
            return []
        if os.path.getsize(self.file_path) == 0:
            return []
        
        with open(self.file_path, "r") as file:
            try:
                data = json.load(file)
            except JSONDecodeError:
                return []
        return data


    def write_accounts_to_file(self, accounts: list[dict]) -> None:
        with open(self.file_path, "w") as file:
            json.dump(accounts, file, indent=4)
    

    def dict_to_account(self, account_dict: dict) -> Account:
        # Handle both old format (owner_id) and new format (user_id)
        user_id = account_dict.get("user_id") or account_dict.get("owner_id")
        
        return Account(
            account_id=account_dict["account_id"],
            user_id=user_id,
            balance=account_dict["balance"]
        )

    def account_to_dict(self, account: Account) -> dict:
        return {
            "account_id": account.account_id,
            "user_id": account.user_id,
            "balance": account.balance
        }

