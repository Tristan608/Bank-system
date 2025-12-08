import json
from models.transaction import Transaction

class TransactionRepository:
    def __init__(self):
        self.file_path = "storage/transactions.json"
    
    def read_transactions_from_file(self) -> list[dict]:
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return data

    def write_transactions_to_file(self, transactions: list[dict]) -> None:
        with open(self.file_path, "w") as file:
            json.dump(transactions, file, indent=4)
    
    def dict_to_transaction(self, transaction_dict: dict) -> Transaction:
        return Transaction(
            transaction_id=transaction_dict["transaction_id"],
            transaction_type=transaction_dict["transaction_type"],
            amount=transaction_dict["amount"],
            sender_id=transaction_dict.get("sender_id"),  # .get means return none instead of crashing
            receiver_id=transaction_dict.get("receiver_id"),
            timestamp=transaction_dict["timestamp"]
        )
    
    def transaction_to_dict(self, transaction: Transaction) -> dict:
        return {
            "transaction_id": transaction.transaction_id,
            "transaction_type": transaction.transaction_type,
            "amount": transaction.amount,
            "sender_id": transaction.sender_id,
            "receiver_id": transaction.receiver_id,
            "timestamp": transaction.timestamp
        }

    

