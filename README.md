# API REST de Produtos – CRUD com FastAPI

API desenvolvida com FastAPI para simular o gerenciamento básico de produtos, com funcionalidades de criação, leitura, atualização e remoção (CRUD).

## Funcionalidades

- Listar produtos com método `GET`
- Obter um produto específico com método `GET`
- Adicionar novos produtos com método `POST`
- Atualizar produtos existentes com método `PUT`
- Remover produtos com método `DELETE`

## Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/) — linguagem de programação utilizada na aplicação
- [FastAPI](https://fastapi.tiangolo.com/) — framework web moderno para APIs
- [Uvicorn](https://www.uvicorn.org/) —  servidor ASGI utilizado para rodar a aplicação
- [Pydantic](https://docs.pydantic.dev/) — biblioteca para validação de dados e definição de schemas
- [Swagger UI](https://swagger.io/tools/swagger-ui/) — interface automática de documentação e teste de rotas

## Como Funciona

1. **GET /produtos**  
   Lista todos os produtos disponíveis.

2. **GET /produtos/{produto_id}**  
   Retorna os detalhes de um produto específico com base no seu ID.

3. **POST /produtos**  
   Cria um novo produto a partir dos dados enviados no corpo da requisição (nome, descrição, preço, disponibilidade).

4. **PUT /produtos/{produto_id}**  
   Atualiza os dados de um produto existente com base no ID informado.

5. **DELETE /produtos/{produto_id}**  
   Remove um produto da lista com base no ID informado.
