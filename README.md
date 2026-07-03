# 📚 API de Livros

API REST desenvolvida com **FastAPI** para gerenciamento de livros. O projeto implementa um **CRUD completo**, permitindo criar, listar, buscar, atualizar e excluir livros.

Tecnologias:

* Python
* FastAPI
* Pydantic
* Uvicorn

Funcionalidades:

* Criar livros
* Listar todos os livros
* Buscar livro por ID
* Atualizar livro
* Excluir livro
* Tratamento de erros com `HTTPException`

Como executar:

Instale as dependências:

```bash
pip install fastapi uvicorn
```

Inicie o servidor:

```bash
uvicorn main:app --reload
```

A API estará disponível em:

* **API:** `http://127.0.0.1:8000`
* **Swagger:** `http://127.0.0.1:8000/docs`
* **ReDoc:** `http://127.0.0.1:8000/redoc`

Endpoints:

| Método | Endpoint             | Descrição               |
| ------ | -------------------- | ----------------------- |
| GET    | `/`                  | Mensagem de boas-vindas |
| POST   | `/livros/criar/`     | Criar um livro          |
| GET    | `/livros/`           | Listar livros           |
| GET    | `/livros/{livro_id}` | Buscar livro por ID     |
| PUT    | `/livros/{livro_id}` | Atualizar livro         |
| DELETE | `/livros/{livro_id}` | Excluir livro           |



