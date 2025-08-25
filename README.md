# Workout API - Gestão de Atletas

![FastAPI](https://img.shields.io/badge/Framework-FastAPI-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)

API REST assíncrona para gerenciar atletas de um centro de treinamento, desenvolvida com FastAPI e SQLAlchemy.

## 🎯 Sobre o Projeto

Este projeto consiste na criação de uma API robusta para gerenciar atletas, categorias e centros de treinamento. O objetivo foi aplicar conceitos avançados de desenvolvimento back-end com Python, incluindo operações assíncronas, manipulação de banco de dados com ORM, validação de dados e boas práticas de desenvolvimento de APIs.

## ✨ Principais Funcionalidades

-   **Cadastro de Atletas:** Endpoint para criar novos atletas com validação de dados.
-   **Consulta de Atletas:** Endpoint para listar todos os atletas com suporte a:
    -   **Filtros:** Busca por nome e CPF através de *query parameters*.
    -   **Paginação:** Sistema de `limit` e `offset` para lidar com grandes volumes de dados.
    -   **Respostas Customizadas:** Retorno de campos específicos para otimizar a visualização.
-   **Tratamento de Erros:** Manipulação específica para exceções de integridade de dados, como o cadastro de um CPF já existente, retornando um status code `303`.

## 🛠️ Tecnologias Utilizadas

-   **[FastAPI](https://fastapi.tiangolo.com/):** Framework web assíncrono para a construção da API.
-   **[SQLAlchemy](https://www.sqlalchemy.org/):** ORM para interação com o banco de dados de forma assíncrona.
-   **[Pydantic](https://docs.pydantic.dev/):** Biblioteca para validação de dados e schemas.
-   **[Uvicorn](https://www.uvicorn.org/):** Servidor ASGI para executar a aplicação.
-   **[fastapi-pagination](https://github.com/uriyyo/fastapi-pagination):** Biblioteca para facilitar a implementação de paginação.
-   **[SQLite](https://www.sqlite.org/index.html):** Banco de dados relacional utilizado via driver `aiosqlite`.

## 🚀 Como Executar

Siga os passos abaixo para rodar o projeto localmente:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/api-atletas-fastapi.git](https://github.com/seu-usuario/api-atletas-fastapi.git)
    cd api-atletas-fastapi
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    uvicorn main:app --reload
    ```

5.  Acesse a documentação interativa no seu navegador: `http://127.0.0.1:8000/docs`

## Endpoints da API

-   `POST /atletas/`: Cria um novo atleta.
-   `GET /atletas/`: Lista todos os atletas (suporta paginação e filtros `?nome=` e `?cpf=`).
