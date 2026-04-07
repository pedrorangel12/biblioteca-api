
# Video da Biblioteca Funcionando:

# https://www.youtube.com/watch?v=sUTPvg8h9f4

-------------------

# Biblioteca API 📚

Uma API REST simples para gerenciar livros, feita com FastAPI, MongoDB e Docker.

## O que esse projeto faz?

Você consegue cadastrar, listar, atualizar e deletar livros. Cada livro tem quatro informações: título, autor, ano de publicação e gênero.

## Tecnologias usadas

- FastAPI
- MongoDB
- Docker e Docker Compose
- PyMongo

## Como rodar o projeto

Você vai precisar ter o Docker instalado na sua máquina.

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/biblioteca-api.git
cd biblioteca-api
```

Sobe a aplicação:

```bash
docker-compose up --build
```

Acessa no navegador:

```
http://localhost:8000/docs
```

Pronto. A documentação interativa já aparece com todos os endpoints disponíveis para testar.

## Endpoints

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | /livros | Lista todos os livros |
| POST | /livros | Cadastra um novo livro |
| GET | /livros/{id} | Busca um livro pelo ID |
| PUT | /livros/{id} | Atualiza um livro |
| DELETE | /livros/{id} | Remove um livro |

## Exemplo de cadastro

```json
{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "ano_publicacao": 1899,
  "genero": "Romance"
}
```

## Estrutura do projeto

```
biblioteca-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── schemas/
│   ├── repositories/
│   ├── services/
│   └── routers/
├── Dockerfile
├── docker-compose.yaml
└── README.md
```

A estrutura segue a arquitetura modular, separando as responsabilidades em camadas: schemas para validação, repositories para acesso ao banco, services para as regras de negócio e routers para as rotas da API.



