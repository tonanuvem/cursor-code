from fastapi import FastAPI, HTTPException, Query, Body, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime
import uuid

app = FastAPI(
    title="Cliente API",
    description="API para gerenciamento de clientes com operações CRUD",
    version="1.0.0"
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Range"]  # Expõe o cabeçalho Content-Range
)

# Modelo do Cliente
class Cliente(BaseModel):
    id: str
    fname: str
    lname: str
    timestamp: str

# Modelo para criação/atualização de cliente
class ClienteCreate(BaseModel):
    fname: str
    lname: str

# Armazenamento em memória (em um caso real, você usaria um banco de dados)
clientes_db = {}

@app.post("/clientes", response_model=Cliente, tags=["Clientes"])
async def criar_cliente(cliente: ClienteCreate):
    """
    Cria um novo cliente.
    """
    novo_cliente = Cliente(
        id=str(uuid.uuid4()),
        fname=cliente.fname,
        lname=cliente.lname,
        timestamp=datetime.now().isoformat()
    )
    clientes_db[novo_cliente.id] = novo_cliente
    return novo_cliente

@app.get("/clientes", tags=["Clientes"])
async def listar_clientes(
    response: Response,
    sort: Optional[str] = Query(None),
    range: Optional[str] = Query(None),
    filter: Optional[str] = Query(None)
):
    """
    Lista clientes com suporte a paginação, ordenação e filtros do react-admin.
    """
    import json
    from operator import attrgetter

    # Converte os clientes para lista
    clientes = list(clientes_db.values())

    # Aplica filtros se existirem
    if filter:
        filtros = json.loads(filter)
        if 'q' in filtros:  # Busca global
            query = filtros['q'].lower()
            clientes = [
                c for c in clientes
                if query in c.fname.lower() or query in c.lname.lower()
            ]

    # Aplica ordenação
    if sort:
        sort_field, sort_order = json.loads(sort)
        reverse = sort_order.lower() == 'desc'
        clientes.sort(key=attrgetter(sort_field), reverse=reverse)

    # Obtém o total antes da paginação
    total = len(clientes)

    # Aplica paginação
    start = 0
    end = total
    if range:
        start, end = json.loads(range)
        clientes = clientes[start:end + 1]

    # Adiciona o cabeçalho Content-Range
    response.headers["Content-Range"] = f"clientes {start}-{end}/{total}"
    
    # Retorna no formato esperado pelo react-admin
    return clientes

@app.get("/clientes/{cliente_id}", response_model=Cliente, tags=["Clientes"])
async def obter_cliente(cliente_id: str):
    """
    Obtém um cliente específico pelo ID.
    """
    if cliente_id not in clientes_db:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return clientes_db[cliente_id]

@app.put("/clientes/{cliente_id}", response_model=Cliente, tags=["Clientes"])
async def atualizar_cliente(cliente_id: str, cliente: ClienteCreate):
    """
    Atualiza os dados de um cliente específico.
    """
    if cliente_id not in clientes_db:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    cliente_atual = clientes_db[cliente_id]
    cliente_atual.fname = cliente.fname
    cliente_atual.lname = cliente.lname
    cliente_atual.timestamp = datetime.now().isoformat()
    
    return cliente_atual

@app.delete("/clientes/{cliente_id}", tags=["Clientes"])
async def deletar_cliente(cliente_id: str):
    """
    Remove um cliente pelo ID.
    """
    if cliente_id not in clientes_db:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    del clientes_db[cliente_id]
    return {"data": {"id": cliente_id}}  # Formato esperado pelo react-admin

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
