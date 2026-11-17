import os
from datetime import datetime
from fastapi import FastAPI

app = FastAPI(title="Meu Primeiro App DevOps")

@app.get("/")
def inicio():
    return {
        "mensagem": "Parabens! Seu aplicativo esta rodando dentro de um conteiner!",
        "ambiente": os.getenv("APP_ENV", "laboratorio-local")
    }

@app.get("/status")
def status():
    return {
        "data_hora": datetime.now().isoformat()
    }

@app.get("/versao")
def versao():
    return {
        "versao": "1.1.0",
        "status": "ok"
    }