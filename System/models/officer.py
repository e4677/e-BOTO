import json
from models.user import User


class Officer(User):
    def __init__(self, officerID, PIN, name):
        super().__init__(officerID, PIN)
        self.name = name

    @classmethod
    def get_officer_by_id(cls, officer_id):
        with open("officer.json", "r") as file:
            officers = json.load(file)
        for officer in officers:
            if officer["officerID"] == officer_id:
                return officer
        return None

    @classmethod
    def authenticate(cls, officerID, PIN):
        with open("officer.json", "r") as file:
            officers = json.load(file)
        for officer in officers:
            if officer.get("officerID") == officerID and officer.get("PIN") == PIN:
                return {"officerID": officer["officerID"], "name": officer["name"]}
        return None
