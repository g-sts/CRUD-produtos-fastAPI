from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

PRODUTOS = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone inteligente",
        "preco": 1999.99,
        "disponivel": True
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um computador portátil",
        "preco": 3999.99,
        "disponivel": False
    }
]

class Produto(BaseModel):
    """Classe de produto."""
    
    nome: str
    descricao: Optional[str] = None
    preco: float
    disponivel: Optional[bool] = True


@app.get("/produtos", tags = ["produtos"])
def listar_produtos() -> list:
    """Listar produtos."""
    return PRODUTOS

@app.get("/produtos/{produto_id}", tags = ["produtos"])
def obter_produto(produto_id: int) -> dict:
    """Obter produto."""
    for produto in PRODUTOS:
        if produto["id"] == produto_id:
            return produto
    return {}

@app.post("/produtos", tags = ["produtos"])
def criar_produto(produto: Produto) -> dict:
    """Criar produto."""
    produto = produto.dict()
    produto["id"] = len(PRODUTOS) + 1
    PRODUTOS.append(produto)
    return produto



