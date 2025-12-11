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
        pass
