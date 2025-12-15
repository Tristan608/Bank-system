import json
from models.user import User

class UserRepository:
    def __init__(self):
        self.file_path = "storage/users.json"
        
        

    def read_users_from_file(self) -> list[dict]:
        try:
            with open(self.file_path, "r") as file:
                content = file.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except FileNotFoundError:
            return []
    
    
    def write_users_to_file(self, users: list[dict]) -> None:
        with open(self.file_path, "w") as file:
            json.dump(users, file, indent=4)
        

    def dict_to_user(self, user_dict: dict) -> User:
        return User(
            user_id=user_dict["user_id"],
            name=user_dict["name"],
            pin=user_dict["pin"],
            role=user_dict["role"]
        )

    def user_to_dict(self, user: User) -> dict:
        return {
            "user_id": user.user_id,
            "name": user.name,
            "pin": user.pin,
            "role": user.role
        }


"""
dict to user:
understand what dict looks like from the models/user.py
in the models/user.py we have a user class with 4 attributes: user_id, name, pin, role
so the dict must look like this when read from the json file:
{
    "user_id": "123",
    "name": "John Doe",
    "pin": "1234",
    "role": "admin"
}

the function must recive one dict and return a User object
============================================================

user to dict:
the function must recive one User object and return a dict




data = json.loads(#string_name)
pritn(data[key][value or index])


indent is to format the json data to be more readable
sort is to sort the keys in alphabetical order

new_json = json.dumps(data, indent=4, sort_keys=True)

read:
r is to read only
json load is to read json data from a file to a python dictionary

with open("file_name.json", "r") as file:
    data = json.load(file)
print(data)

write:
w is to write only
json dump is to write python dictionary data to a json file

with open("file_name.json", "w") as file:
    json.dump(data, file, indent=4)



 def read_users_from_file(self) -> list[dict]:
        # Gracefully handle missing or empty files
        if not os.path.exists(self.file_path):
            return []
        if os.path.getsize(self.file_path) == 0:
            return []

        with open(self.file_path, "r") as file:
            try:
                data = json.load(file)
            except JSONDecodeError:
                # If file is corrupt/empty, treat as no users
                return []
        return data
"""
