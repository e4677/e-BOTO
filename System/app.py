from flask import Flask, jsonify, request
from flask_cors import CORS
from services.voter_service import VoterService
from services.candidate_service import CandidateService
from services.officer_service import OfficerService
from services.voting_service import VotingService

app = Flask(__name__)
CORS(app)

#For the Voter

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    voterID = data.get("voterID")
    PIN = data.get("PIN")

    voter_data = VoterService.login(voterID, PIN)

    if voter_data:
        return jsonify({"message": "Login successful!", "voter": voter_data}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


@app.route("/voter/<voter_id>", methods=["GET"])
def get_voter_info(voter_id):
    voter = VoterService.get_voter_info(voter_id)

    if voter:
        return jsonify(voter), 200
    return jsonify({"message": "Voter not found"}), 404


@app.route("/candidates", methods=["GET"])
def get_candidates():
    candidates_data = CandidateService.get_candidates()
    return jsonify(candidates_data)


@app.route("/submit_vote", methods=["POST"])
def submit_vote():
    data = request.json
    voter_id = data.get("voterID")
    vote_data = data.get("candidates")

    CandidateService.update_vote(vote_data)

    if VoterService.update_voter_status(voter_id):
        return jsonify({"message": "Vote submitted and hasVoted updated!"}), 200
    else:
        return jsonify({"error": "Voter not found or error updating status"}), 404


@app.route("/update_voter_status", methods=["POST"])
def update_voter_status():
    data = request.json
    voterID = data.get("voterID")

    if not voterID:
        return jsonify({"error": "No voterID provided!"}), 400

    if VoterService.update_voter_status(voterID):
        return jsonify({"message": "Voter status updated successfully."}), 200
    else:
        return jsonify({"error": "Voter not found!"}), 404

#For the Officer

@app.route("/voting_status", methods=["GET"]) 
def get_voting_status():
    return jsonify({"isVotingOpen": VotingService.voting_status})

@app.route("/open_voting", methods=["POST"])
def open_voting():
    if VotingService.set_voting_status(True):
        return jsonify({"message": "Voting is now open."}), 200
    return jsonify({"error": "Failed to open voting."}), 500

@app.route("/close_voting", methods=["POST"])
def close_voting():
    if VotingService.set_voting_status(False):
        return jsonify({"message": "Voting is now closed."}), 200
    return jsonify({"error": "Failed to close voting."}), 500

@app.route("/officer/login", methods=["POST"])
def officer_login():
    data = request.json
    officerID = data.get("officerID")
    PIN = data.get("PIN")
    
    officer_data = OfficerService.login(officerID, PIN)
    
    if officer_data:
        return jsonify({"message": "Login successful!", "officer": officer_data}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
    
@app.route("/vote_count", methods=["GET"])
def get_vote_count():
    vote_results = CandidateService.get_vote_count()
    print("Vote Results:", vote_results)  
    return jsonify(vote_results)


if __name__ == "__main__":
    app.run(debug=True)
