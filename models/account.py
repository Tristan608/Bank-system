class Account:
    def __init__(self, account_id: str, owner_id: str, balance: float):
        self.account_id = account_id
        self.owner_id = owner_id
        self.balance = balance
    
    def __repr__(self):
        return f"Account(account_id={self.account_id}, owner_id={self.owner_id}, balance={self.balance})"
    