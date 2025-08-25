# main.py
from fastapi import FastAPI
from controller import router as atleta_router
from models import Base
from database import engine
from fastapi_pagination import add_pagination

app = FastAPI(title="Workout API")

# Adiciona as rotas do controller
app.include_router(atleta_router, prefix='/atletas', tags=['atletas'])

# Adiciona o middleware de paginação
add_pagination(app)

@app.on_event("startup")
async def startup():
    # Criar as tabelas no banco de dados
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)