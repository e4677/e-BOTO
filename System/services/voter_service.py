from models.voter import Voter
from services.main_service import MainService


class VoterService(MainService):
    VOTER_FILE = "voters.json"

    @staticmethod
    def login(voterID, PIN):
        return MainService.login(Voter, voterID, PIN, VoterService.VOTER_FILE)

    @staticmethod
    def get_voter_info(voter_id):
        return Voter.get_voter_by_id(voter_id)

    @staticmethod
    def update_voter_status(voter_id):
        return Voter.update_voter_status(voter_id)
