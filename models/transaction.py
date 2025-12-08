class Transaction:
    def __init__(self, transaction_id: str, transaction_type: str, amount: float, sender_id: str | None, receiver_id: str | None, timestamp: str):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type  # deposit, withdrawal, transfer
        self.amount = amount
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.timestamp = timestamp

    def __repr__(self):
        return ( 
            f"Transaction(id={self.transaction_id}, "
            f"type={self.transaction_type}, amount={self.amount}, "
            f"sender_id={self.sender_id}, receiver={self.receiver_id}, "
            f"timestamp={self.timestamp})"
        )
        