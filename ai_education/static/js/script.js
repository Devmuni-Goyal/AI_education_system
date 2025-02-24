// script.js

document.addEventListener("DOMContentLoaded", function() {
    // Change background color to white
    document.body.style.backgroundColor = "#FFFFFF";

    // Change font size of all elements to 15px
    document.body.style.fontSize = "15px";
});

// Toggle Chatbot Window
function toggleChatbot() {
    var chatbot = document.getElementById("chatbot");
    chatbot.style.display = (chatbot.style.display === "flex") ? "none" : "flex";
}

// Handle Enter Key for Sending Message
function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

// Send Message Function
function sendMessage() {
    var inputField = document.getElementById("user-input");
    var userText = inputField.value.trim();
    
    if (userText === "") return; // Empty message check

    addMessage(userText, "user-message");
    inputField.value = ""; // Clear input field

    // Simulated bot response (Backend integration needed here)
    setTimeout(() => {
        var botReply = "I am AI Chatbot! How can I help you?";
        addMessage(botReply, "bot-message");
    }, 1000);
}

// Add Message to Chatbox
function addMessage(text, className) {
    var messageContainer = document.getElementById("chatbot-messages");
    var messageDiv = document.createElement("div");
    messageDiv.className = "message " + className;
    messageDiv.textContent = text;
    messageContainer.appendChild(messageDiv);
    
    // Auto Scroll to Bottom
    messageContainer.scrollTop = messageContainer.scrollHeight;
}


