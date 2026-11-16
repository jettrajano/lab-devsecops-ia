import os
from fastapi import FastAPI

app = FastAPI(title="Meu Primeiro App DevOps")

@app.get("/")
def inicio():
    return {
        "mensagem": "Parabens! Seu aplicativo esta rodando dentro de um conteiner!",
        "ambiente": os.getenv("APP_ENV", "laboratorio-local")
    }