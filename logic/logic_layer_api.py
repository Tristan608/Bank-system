from models.transaction import Transaction
from models.account import Account
from models.user import User
from logic.account_manager import AccountManager
from logic.user_manager import UserManager
from logic.transaction_manager import TransactionManager

class LogicLayerAPI:
    def __init__(self, data_layer):
        self.user_manager = UserManager(data_layer)  # Dependency Injection DI, pass data layer to managers!
        self.account_manager = AccountManager(data_layer)
        self.transaction_manager = TransactionManager(data_layer)
    
    def login(self, user_id: int, pin: int) -> User | None:
        return self.user_manager.login(user_id, pin)
    
    def create_user(self, name: str, pin: int, role: str) -> User:
        return self.user_manager.create_user(name, pin, role)
    
    def create_account(self, user_id: int, starting_balance: float) -> Account:
        return self.account_manager.create_account(user_id, starting_balance)
    
    def view_all_users(self) -> list[User]:
        return self.user_manager.view_all_users()
    
    def view_all_accounts(self) -> list[Account]:
        return self.account_manager.view_all_accounts()
    
    def view_balance(self, account_id: int) -> float:
        return self.account_manager.view_balance(account_id)
    
    def deposit(self, amount: float, account_id: int) -> None:
        self.transaction_manager.deposit(amount, account_id)

    def withdraw(self, amount: float, account_id: int) -> None:
        self.transaction_manager.withdraw(amount, account_id)
    
    def transfer(self, amount: float, reciever_id: int, sender_id: int) -> None:
        self.transaction_manager.transfer(amount, reciever_id, sender_id)
    
    def view_transaction_history(self, account_id: int) -> list[Transaction]:
        return self.transaction_manager.view_transaction_history(account_id)
    
    def view_bank_info(self) -> dict:
        return {
            "name": "Mini Bank",
            "version": "1.0",
            "currency": "USD"
        }
    
    def read_system_instructions(self) -> str:
        return "Welcome to Mini Bank! Use this system to manage your accounts and transactions securely."

    

