import json


class User:
    def __init__(self, user_id, name, pin):
        self.__user_id = user_id
        self.name = name
        self.__pin = pin

    def get_user_id(self):
        return self.__user_id

    def get_pin(self):
        return self.__pin

    @classmethod
    def authenticate(cls, user_id, pin, file_name):
        users = cls.load_users(file_name)
        user = users.get(user_id)
        if user and user.get_pin() == pin:
            return user
        return None

    @classmethod
    def load_users(cls, file_name):
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                return {id: cls(id, info["name"], info["PIN"]) for id, info in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
