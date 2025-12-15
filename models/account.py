class Account:
    def __init__(self, account_id: str, user_id: str, balance: float):
        self.account_id = account_id
        self.user_id = user_id
        self.balance = balance
    
    def __repr__(self):
        return f"Account(account_id={self.account_id}, user_id={self.user_id}, balance={self.balance})"
    