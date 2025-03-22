from .user import User
import json

class Voter(User):
    def __init__(self, voterID, PIN, name, birthdate, address, hasVoted=False):
        super().__init__(voterID, name, PIN)
        self.birthdate = birthdate
        self.address = address
        self.hasVoted = hasVoted

    @classmethod
    def get_voter_by_id(cls, voter_id):
        with open("voters.json", "r") as file:
            voters = json.load(file)
        for voter in voters:
            if voter["voterID"] == voter_id:
                return voter
        return None

    @classmethod
    def update_voter_status(cls, voter_id):
        with open("voters.json", "r") as file:
            voters = json.load(file)

        for voter in voters:
            if voter["voterID"] == voter_id:
                voter["hasVoted"] = True
                break
        else:
            return False

        with open("voters.json", "w") as file:
            json.dump(voters, file, indent=4)
        return True

    @classmethod
    def authenticate(cls, voterID, PIN):
        with open("voters.json", "r") as file:
            voters = json.load(file)
        for voter in voters:
            if voter.get("voterID") == voterID and voter.get("PIN") == PIN:
                voter_data = {key: voter[key] for key in voter if key != "PIN"}
                return voter_data
        return None
