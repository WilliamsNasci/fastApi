from operator import index
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Cliente(BaseModel):
    id: Optional[int]
    nome: str
    idade: int
    sexo: str
    
dados: List[Cliente] = []
        
@app.get("/clientes")
def listar_clientes():
    return dados

@app.get("/clientes/{id_cliente}")
def obter_cliente(id_cliente: str):
    for cliente in dados:
        if cliente.id == id_cliente:
            return cliente
    return {"error": "Cliente nao existe."}

@app.post("/clientes")
def cadastra_cliente(cliente: Cliente):
    cliente.id = str(uuid4())
    dados.append(cliente)
    return {"msg": f"Cliente {cliente.nome} cadastrado com sucesso!"}


@app.delete("/clientes/{id_cliente}")
def deleta_cliente(id_cliente: str):
    posicao = -1
    for index, cliente in enumerate(dados):
        if cliente.id == id_cliente:
            posicao = index
            break
    if posicao != -1:
        dados.pop(posicao)
        return {"msg": "Cliente removido com sucesso!"}
    else:
        return {"error": "Cliente nao encontrado"}