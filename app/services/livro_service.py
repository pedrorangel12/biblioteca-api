from repositories.livro_repository import *

def format_livro(livro):
    livro["_id"] = str(livro["_id"])
    return livro

def create_livro_service(livro):
    result = create_livro(livro.model_dump())
    return {"message": "Livro criado com sucesso", "id": str(result.inserted_id)}

def get_all_livros_service():
    livros = get_all_livros()
    return [format_livro(livro) for livro in livros]

def get_livro_by_id_service(livro_id):
    try:
        livro = get_livro_by_id(livro_id)
    except:
        return {"error": "ID inválido"}
    if not livro:
        return {"error": "Livro não encontrado"}
    return format_livro(livro)

def update_livro_service(livro_id, livro):
    try:
        result = update_livro(livro_id, livro.model_dump())
    except:
        return {"error": "ID inválido"}
    if result.matched_count == 0:
        return {"error": "Livro não encontrado"}
    return {"message": "Livro atualizado com sucesso"}

def delete_livro_service(livro_id):
    try:
        result = delete_livro(livro_id)
    except:
        return {"error": "ID inválido"}
    if result.deleted_count == 0:
        return {"error": "Livro não encontrado"}
    return {"message": "Livro deletado com sucesso"}