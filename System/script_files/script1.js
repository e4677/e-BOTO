//SCRIPT FOR VOTER REGISTRATION
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("loginForm").addEventListener("submit", async function(event) {
        event.preventDefault(); 

        let voterID = document.getElementById("voterid").value;
        let PIN = document.getElementById("voterpin").value;

        try {
            let response = await fetch("http://127.0.0.1:5000/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ voterID, PIN })  
            });

            let result = await response.json();  

            if (response.ok) {
                
                sessionStorage.setItem("voterID", voterID);
                console.log("voterID stored:", voterID);  
                alert("✅ Login successful!");
                window.location.href = "voting_home.html";  
            } else {
                alert(result.message);  
            }
        } catch (error) {
            console.error("⚠️ Error:", error);
            alert("⚠️ Server error. Please try again later.");
        }
    });
});