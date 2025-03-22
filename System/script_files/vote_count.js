document.addEventListener("DOMContentLoaded", function () {
    fetchVoteCount();
});

function fetchVoteCount() {
    fetch("http://127.0.0.1:5000/vote_count")
        .then(response => response.json())
        .then(data => {
            console.log("Vote Count Data:", data); 

            const tableBody = document.getElementById("voteTableBody");
            if (!tableBody) {
                console.error("Table body not found!");
                return;
            }

            tableBody.innerHTML = ""; 

            const positionOrder = ["mayor", "councilor"]; 

            let positions = Object.keys(data.candidates);

            positions.sort((a, b) => {
                let indexA = positionOrder.indexOf(a.toLowerCase());
                let indexB = positionOrder.indexOf(b.toLowerCase());

                if (indexA === -1) indexA = Infinity; 
                if (indexB === -1) indexB = Infinity;

                return indexA - indexB;
            });

            positions.forEach(position => {
                const candidates = data.candidates[position];

                const positionRow = document.createElement("tr");
                positionRow.innerHTML = `<td colspan="2"><strong>${position.toUpperCase()}</strong></td>`;
                tableBody.appendChild(positionRow);

                candidates.forEach(candidate => {
                    const row = document.createElement("tr");
                    row.innerHTML = `<td>${candidate.name}</td><td>${candidate.votecount}</td>`;
                    tableBody.appendChild(row);
                });
            });
        })
        .catch(error => console.error("Error fetching vote count:", error));
}