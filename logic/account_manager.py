from models.account import Account
from data.data_layer_api import DataLayerAPI
import random

class AccountManager:
    def __init__(self, data_layer: DataLayerAPI):
        self.data_layer = data_layer
    
    def create_account(self, user_id, starting_balance):
        # load all accounts
        accounts = self.data_layer.load_accounts()

        # generate new account_id
        new_id = random.randint(100000, 999999)
        while any(account.account_id == new_id for account in accounts):
            new_id = str(random.randint(100000, 999999))
        
        # create new account object
        new_account = Account(new_id, user_id, starting_balance)

        # add to accounts list and save
        accounts.append(new_account)
        self.data_layer.save_accounts(accounts)
        return new_account
    

    def view_all_accounts(self):
        return self.data_layer.load_accounts()
    

    def view_balance(self, account_id):
        accounts = self.data_layer.load_accounts()
        for account in accounts:
            if account.account_id == account_id:
                return account.balance
        return None
    


