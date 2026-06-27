const welcomeCard = document.getElementById("welcomeCard");
const closeWelcomeButton = document.getElementById("closeWelcome");
const chatForm = document.getElementById("chatForm");
const typing = document.getElementById("typing");
const messages = document.getElementById("messages");

closeWelcomeButton.addEventListener("click", () => {
    welcomeCard.style.opacity = "0";
    welcomeCard.style.transform = "scale(0.95)";

    setTimeout(() => {
        welcomeCard.style.display = "none";
    }, 300);
});

chatForm.addEventListener("submit", () => {
    typing.style.display = "block";
});

messages.scrollTop = messages.scrollHeight;
