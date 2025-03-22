import json


class MainService:
    @classmethod
    def load_data(cls, file_name):
        """Load data from a JSON file."""
        try:
            with open(file_name, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @classmethod
    def login(cls, user_class, user_id, pin, file_name):
        """Authenticate user using provided class and file."""
        user = user_class.authenticate(user_id, pin)
        if user:
            return user
        return None
