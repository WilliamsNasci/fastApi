from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Hello, World!"}

class Produto(BaseModel):
    name: str
    price: float

@app.post("/produtos")
def produtos(produto: Produto):
    return {"mensagem": f"Produto ({produto.name} - R$ {produto.price:.2f}) cadastrado com sucesso!"}

    