//SCRIPT FOR VOTING BALLOT
async function loadCandidates() {
    try {
        const response = await fetch('http://127.0.0.1:5000/candidates');
        const data = await response.json();

        const mayorDiv = document.getElementById("mayorCandidates");
        const councilorDiv = document.getElementById("councilorCandidates");

        if (data.candidates.mayor) {
            mayorDiv.innerHTML = data.candidates.mayor.map(candidate =>
                `<input type="radio" name="mayor" value="${candidate.candidateID}" data-name="${candidate.name}"> ${candidate.name}<br>`
            ).join('');
        }

        if (data.candidates.councilor) {
            councilorDiv.innerHTML = data.candidates.councilor.map(candidate =>
                `<input type="checkbox" name="councilor" value="${candidate.candidateID}" data-name="${candidate.name}"> ${candidate.name}<br>`
            ).join('');
        }
    } catch (error) {
        console.error("Error fetching candidates:", error);
    }
}

function saveSelectedCandidates(event) {
    event.preventDefault();

    const selectedMayor = document.querySelector('input[name="mayor"]:checked');
    const mayorChoice = selectedMayor
        ? { position: "Mayor", candidate: selectedMayor.dataset.name }
        : null;

    const selectedCouncilors = Array.from(document.querySelectorAll('input[name="councilor"]:checked'));
    const councilorChoices = selectedCouncilors.map(councilor => ({
        position: "Councilor",
        candidate: councilor.dataset.name
    }));

    const selectedCandidates = [];
    if (mayorChoice) selectedCandidates.push(mayorChoice);
    selectedCandidates.push(...councilorChoices);

    localStorage.setItem('selectedCandidates', JSON.stringify(selectedCandidates));

    window.location.href = 'voting_review.html';
}

window.onload = loadCandidates;
document.getElementById('ballotForm').addEventListener('submit', saveSelectedCandidates);