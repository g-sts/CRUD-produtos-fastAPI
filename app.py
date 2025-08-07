from fastapi import FastAPI

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

