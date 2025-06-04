# cursor-code

## API de Clientes

Esta é uma API RESTful para gerenciamento de clientes implementada com FastAPI.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando a API

Para iniciar o servidor:

```bash
python main.py
```

Ou diretamente com uvicorn:

```bash
uvicorn main:app --reload
```

O servidor estará disponível em `http://localhost:8000`

## Documentação da API (Swagger UI)

Acesse a documentação interativa em: `http://localhost:8000/docs`

## Endpoints

### Criar Cliente
- **POST** `/clientes/`
- Parâmetros:
  - fname (string): Nome do cliente
  - lname (string): Sobrenome do cliente

### Listar Clientes
- **GET** `/clientes/`
- Lista todos os clientes cadastrados

### Obter Cliente
- **GET** `/clientes/{cliente_id}`
- Obtém os detalhes de um cliente específico

### Atualizar Cliente
- **PUT** `/clientes/{cliente_id}`
- Parâmetros opcionais:
  - fname (string): Novo nome
  - lname (string): Novo sobrenome

### Deletar Cliente
- **DELETE** `/clientes/{cliente_id}`
- Remove um cliente do sistema

## Estrutura do Cliente

```json
{
    "id": "string",
    "fname": "string",
    "lname": "string",
    "timestamp": "string"
}
```

- `id`: Identificador único gerado automaticamente
- `fname`: Nome do cliente
- `lname`: Sobrenome do cliente
- `timestamp`: Data e hora da última atualização 
