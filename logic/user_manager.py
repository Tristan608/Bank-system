from models.user import User
from data.data_layer_api import DataLayerAPI
import random

class UserManager:
    def __init__(self, data_layer: DataLayerAPI):
        self.data_layer = data_layer
    
    def login(self, user_id, pin):
        # load all users
        users = self.data_layer.load_users()

        # find user with matching user_id and pin
        for user in users:
            if user.user_id == user_id and user.pin == pin:
                return user
          
        return None

    def create_user(self, name, pin, role):
        # load all users
        users = self.data_layer.load_users()

        # generate new user_id
        new_id = "U" + str(random.randint(1000, 9999))
        while any(user.user_id == new_id for user in users):
            new_id = "U" + str(random.randint(1000, 9999))


        # create new user object
        new_user = User(new_id, name, pin, role)

        # add to users list and save
        users.append(new_user)

        # save to data layer
        self.data_layer.save_users(users)

        return new_user

    def logout(self, user: User):
        pass
    