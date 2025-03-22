import json


class Candidate:
    @classmethod
    def get_all_candidates(cls):
        with open("candidates.json", "r") as file:
            candidates_data = json.load(file)
        return candidates_data

    @classmethod
    def update_candidate_votes(cls, vote_data):
        with open("candidates.json", "r") as file:
            candidates_data = json.load(file)

        for vote in vote_data:
            position = vote["position"].lower()
            if position in candidates_data["candidates"]:
                for candidate in candidates_data["candidates"][position]:
                    if candidate["name"] == vote["candidate"]:
                        candidate["votecount"] += 1

        with open("candidates.json", "w") as file:
            json.dump(candidates_data, file, indent=4)
