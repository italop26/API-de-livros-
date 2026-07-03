from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Livro(BaseModel):
    titulo: str
    autor: str
    ano_publicacao: int

livros_db = {}
proximo_id = 1

# Endpoints da API:

@app.get("/")
def iniciar():
    return {"message": "Bem-vindo à API de Livros!"}

# Endpoint para criar um novo livro
@app.post("/livros/criar/", status_code=201)
def criar_livro(livro: Livro):
    global proximo_id
    livros_db[proximo_id] = livro.model_dump()
    livros_db[proximo_id]["id"] = proximo_id
    proximo_id += 1
    return livros_db[proximo_id - 1]

# listar todos os livros 
@app.get("/livros/")
def listar_livros():
    return list(livros_db.values())

# procurar um livro pelo ID com path parameter
@app.get("/livros/{livro_id}")
def procurar_livro(livro_id: int):
    if livro_id not in livros_db:
        raise HTTPException(status_code=404, detail='livro não encontrado')
    return livros_db[livro_id]

#deletar um livro pelo ID com path parameter
@app.delete("/livros/{livro_id}", status_code=204)
def deletar_livro(livro_id: int):
    if livro_id not in livros_db:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    del livros_db[livro_id]

#procurar um livro pelo ID com path parameter e atualizar as informações do livro
@app.put("/livros/{livro_id}")
def atualizar(livro_id: int, livro: Livro):
    if livro_id not in livros_db:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    livros_db[livro_id] = livro.model_dump()
    livros_db[livro_id]["id"] = livro_id
    return livros_db[livro_id]


