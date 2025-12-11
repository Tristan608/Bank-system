from models.transaction import Transaction
from data.data_layer_api import DataLayerAPI
import random
import datetime



class TransactionManager:
    def __init__(self, data_layer: DataLayerAPI):
        self.data_layer = data_layer
        
    
    def deposit(self, amount, account_id):
        # update balance using AccountManager
        accounts = self.data_layer.load_accounts()

        target_account = None
        for account in accounts:
            if account.account_id == account_id:
                account.balance += amount
                target_account = account
                break
        
        if target_account is None:
            raise ValueError("Account not found")  
        
        self.data_layer.save_accounts(accounts)


        # load existing transactions
        transactions = self.data_layer.load_transactions()

        # create new transaction object
        transaction_id = "T" + str(random.randint(100000, 999999))
        timestamp = datetime.datetime.now().isoformat()

        new_transaction = Transaction(
            transaction_id=transaction_id,
            transaction_type="deposit",
            amount=amount,
            sender_id=None,
            receiver_id=account_id,
            timestamp=timestamp
        )


        # add to list and save
        transactions.append(new_transaction)
        self.data_layer.save_transactions(transactions)

    def withdraw(self, amount, account_id):
        #  get accounts
        accounts = self.data_layer.load_accounts()

        target_account = None
        for account in accounts:
            if account.account_id == account_id:
                target_account = account
                break   
        
        if target_account is None:
            raise ValueError("Account not found")
        
        if target_account.balance < amount:
            raise ValueError("Insufficient funds")
        
        target_account.balance -= amount

        self.data_layer.save_accounts(accounts)

        # load existing transactions
        transactions = self.data_layer.load_transactions()

        # create new transaction object
        transaction_id = "T" + str(random.randint(100000, 999999))
        timestamp = datetime.datetime.now().isoformat()

        new_transaction = Transaction(
            transaction_id=transaction_id,
            transaction_type="withdraw",
            amount=amount,
            sender_id=account_id,
            receiver_id=None,
            timestamp=timestamp
        )   

        # add to list and save
        transactions.append(new_transaction)
        self.data_layer.save_transactions(transactions)


    def transfer(self, amount, reciever_id, sender_id):
        # get accounts
        accounts = self.data_layer.load_accounts()

        sender_account = None
        receiver_account = None

        for account in accounts:
            if account.account_id == sender_id:
                sender_account = account
            if account.account_id == reciever_id:
                receiver_account = account

        if sender_account is None:
            raise ValueError("Sender account not found")
        if receiver_account is None:
            raise ValueError("Receiver account not found")
        if sender_account.balance < amount:
            raise ValueError("Insufficient funds in sender account")
        
        sender_account.balance -= amount
        receiver_account.balance += amount

        self.data_layer.save_accounts(accounts)

        # load existing transactions
        transactions = self.data_layer.load_transactions()
        # create new transaction object
        transaction_id = "T" + str(random.randint(100000, 999999))
        timestamp = datetime.datetime.now().isoformat()


        new_transaction = Transaction(
            transaction_id=transaction_id,
            transaction_type="transfer",
            amount=amount,
            sender_id=sender_id,
            receiver_id=reciever_id,
            timestamp=timestamp
        )

        # add to list and save
        transactions.append(new_transaction)
        self.data_layer.save_transactions(transactions)


    def view_transaction_history(self, account_id):
        # load transactions
        transactions = self.data_layer.load_transactions()

        # filter by account_id
        account_transactions = [
            tx for tx in transactions
            if tx.sender_id == account_id or tx.receiver_id == account_id
        ]
        return account_transactions
    
        



