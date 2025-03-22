//SCRIPT FOR VOTE REVIEW PAGE
function loadSelectedCandidates() {
    const selectedCandidates = JSON.parse(localStorage.getItem('selectedCandidates')) || [];

    const table = document.querySelector(".vote_review table");

    table.innerHTML = `
        <tr>
            <th>Position</th>
            <th>Candidate</th>
        </tr>
    `;

    selectedCandidates.forEach(candidate => {
        const row = `
            <tr>
                <td>${candidate.position}</td>
                <td>${candidate.candidate}</td>
            </tr>
        `;
        table.innerHTML += row;
    });
}

window.onload = loadSelectedCandidates;