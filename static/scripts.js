const chatLog = document.getElementById('chat-log');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const chatUrl = "{% url 'web_app:chatapp_chatbot' %}";
sendButton.addEventListener('click', () => {
    const message = userInput.value;
    if (message.trim() !== '') { // Prevent empty messages
        displayMessage('user', message);
        sendMessageToBackend(message);
        userInput.value = ''; // Clear the input field
    }
});

function displayMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.textContent = message;
    chatLog.appendChild(messageElement);
}

function sendMessageToBackend(message) {
    fetch('chat/', { 
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message }),
    })
    .then(response => response.json())
    .then(data => {
        displayMessage('bot', data.response);
    });
}