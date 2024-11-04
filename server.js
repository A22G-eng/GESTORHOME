require("dotenv").config()     // Carrega variáveis de ambiente do arquivo .env
const express = require('express'); // Importa o Express
const mongoose = require('mongoose'); // Importa o Mongoose
console.log("MONGO_URI:", MONGO_URI);


const app = express();              // Cria uma instância do Express

// Conecte ao MongoDB (se já tiver o URI no .env)
mongoose.connect(process.env.DB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("Conectado ao MongoDB"))
  .catch((err) => console.error("Erro ao conectar ao MongoDB", err));

// Define uma rota básica
app.get("/", (req, res) => {
  res.send("Bem-vindo ao Gestorhome!");
});

// Configura o servidor para rodar na porta 5500
const PORT = process.env.PORT || 5500;
app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});
