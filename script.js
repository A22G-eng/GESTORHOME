// Obtendo referências aos elementos do DOM
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const chatMessages = document.querySelector('.chat-messages');

// Função para enviar a mensagem do usuário
function sendMessage(event) {
    event.preventDefault(); // Evitar o envio do formulário padrão

    const message = userInput.value.trim(); // Captura a mensagem do usuário

    if (message) {
        // Adiciona a mensagem do usuário ao chat
        addMessage('Você: ' + message);

        // Limpa o campo de entrada
        userInput.value = '';

        // Envia a mensagem para o chatbot
        getResponseFromChatbot(message);
    }
}

// Função para adicionar mensagens à interface
function addMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    chatMessages.appendChild(messageElement);
}

// Função para obter a resposta do chatbot (simulação)
function getResponseFromChatbot(userMessage) {
    // Aqui você deve fazer uma chamada para o seu backend que contém o chatbot
    // Por simplicidade, vamos simular uma resposta
    setTimeout(() => {
        const simulatedResponse = "Assistente: " + simulateChatbotResponse(userMessage);
        addMessage(simulatedResponse);
    }, 1000); // Simula um atraso de 1 segundo
}

// Função para simular a resposta do chatbot (substitua isso pela chamada real ao backend)
function simulateChatbotResponse(message) {
    // Aqui você pode implementar lógica simples ou retornar respostas fixas
    return "Você disse: " + message;
}

// Adiciona o listener para o botão de envio
sendButton.addEventListener('click', sendMessage);

// Adiciona o listener para pressionar Enter
userInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage(event);
    }
});