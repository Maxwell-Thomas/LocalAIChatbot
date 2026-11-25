
const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");
const chatArea = document.getElementById("chatArea");
const sendButton = document.getElementById("sendButton");
const clearChat = document.getElementById("clearChat");
const welcomeScreen = document.getElementById("welcomeScreen");

let messages = [];

function addMessage(role, content) {
    const message = document.createElement("div");

    message.className =
        role === "user"
            ? "message user-message"
            : "message ai-message";

    if (role === "assistant") {
        const label = document.createElement("div");
        label.className = "message-label";
        label.textContent = "LOCAL AI";
        message.appendChild(label);
    }

    const text = document.createElement("div");
    text.textContent = content;

    message.appendChild(text);
    chatArea.appendChild(message);

    chatArea.scrollTop = chatArea.scrollHeight;
}

async function sendMessage(prompt) {
    if (!prompt.trim()) return;

    welcomeScreen.style.display = "none";

    messages.push({
        role: "user",
        content: prompt
    });

    addMessage("user", prompt);

    userInput.value = "";
    sendButton.disabled = true;

    const loading = document.createElement("div");
    loading.className = "typing";
    loading.textContent = "AI is thinking...";

    chatArea.appendChild(loading);

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                messages: messages
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "AI service error");
        }

        const answer = data.response;

        messages.push({
            role: "assistant",
            content: answer
        });

        loading.remove();
        addMessage("assistant", answer);

    } catch (error) {
        loading.remove();

        // Remove the failed message from conversation history.
        messages.pop();

        addMessage(
            "assistant",
            "Error: " + error.message
        );

        console.error(error);

    } finally {
        sendButton.disabled = false;
        userInput.focus();
    }
}

chatForm.addEventListener("submit", function(event) {
    event.preventDefault();
    sendMessage(userInput.value);
});

userInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        chatForm.requestSubmit();
    }
});

document.querySelectorAll(".suggestion").forEach(button => {
    button.addEventListener("click", function() {
        sendMessage(this.textContent);
    });
});

clearChat.addEventListener("click", function() {
    messages = [];

    chatArea.innerHTML = "";
    chatArea.appendChild(welcomeScreen);

    welcomeScreen.style.display = "flex";
});

