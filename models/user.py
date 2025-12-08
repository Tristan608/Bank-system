class User:
    def __init__(self, user_id: str, name: str, pin: str, role: str):
        self.user_id = user_id
        self.name = name
        self.pin = pin
        self.role = role # admin or user
    
    def __repr__(self):
        return f"User(user_id={self.user_id}, name={self.name}, role={self.role})"
    
