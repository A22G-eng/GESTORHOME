from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Carregando o modelo de linguagem
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = chatbot(user_message)
    return jsonify({'response': response[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)