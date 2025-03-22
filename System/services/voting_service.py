class VotingService:
    votes = {}  
    voting_status = False  

    @classmethod
    def submit_vote(cls, voter_id, votes):
        if not cls.voting_status:
            return {"success": False, "message": "Voting is closed", "status": 403}

        if voter_id in cls.votes:
            return {"success": False, "message": "Voter has already voted", "status": 400}

        cls.votes[voter_id] = votes
        return {"success": True, "message": "Vote submitted successfully", "status": 200}

    @classmethod
    def get_vote_count(cls):
        results = {}
        for vote_list in cls.votes.values():
            for vote in vote_list:
                results[vote] = results.get(vote, 0) + 1
        return results

    @classmethod
    def get_voting_status(cls):
        return cls.voting_status

    @classmethod
    def set_voting_status(cls, status):
        cls.voting_status = status
        return True
