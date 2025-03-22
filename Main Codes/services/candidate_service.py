from models.candidate import Candidate
import json


class CandidateService:
    @staticmethod
    def get_candidates():
        return Candidate.get_all_candidates()

    @staticmethod
    def update_vote(vote_data):
        Candidate.update_candidate_votes(vote_data)

    @staticmethod
    def get_vote_count():
        try:
            with open("candidates.json", "r") as file:
                data = json.load(file)
            return data  
        except FileNotFoundError:
            return {"error": "Candidates data file not found"}
        except json.JSONDecodeError:
            return {"error": "Error reading candidates data file"}