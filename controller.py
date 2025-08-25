# controller.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination import Page, LimitOffsetPage, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate

from models import Atleta, Categoria, CentroTreinamento
from schemas import AtletaIn, AtletaListOut
from database import get_session

router = APIRouter()

@router.post(
    '/',
    summary='Criar um novo atleta',
    status_code=201,
)
async def create_atleta(
    atleta_in: AtletaIn,
    db_session: AsyncSession = Depends(get_session)
):
    # Requisito 3: Manipular exceção de integridade dos dados
    try:
        # Busca Categoria e CT pelos nomes
        categoria = (await db_session.execute(select(Categoria).filter_by(nome=atleta_in.categoria))).scalars().first()
        if not categoria:
            raise HTTPException(status_code=400, detail=f"A categoria {atleta_in.categoria} não foi encontrada.")
        
        ct = (await db_session.execute(select(CentroTreinamento).filter_by(nome=atleta_in.centro_treinamento))).scalars().first()
        if not ct:
            raise HTTPException(status_code=400, detail=f"O centro de treinamento {atleta_in.centro_treinamento} não foi encontrado.")

        atleta = Atleta(
            nome=atleta_in.nome,
            cpf=atleta_in.cpf,
            idade=atleta_in.idade,
            peso=atleta_in.peso,
            altura=atleta_in.altura,
            sexo=atleta_in.sexo,
            categoria_id=categoria.id,
            centro_treinamento_id=ct.id
        )
        
        db_session.add(atleta)
        await db_session.commit()

    except IntegrityError:
        # Nota: O status code 409 Conflict é mais comum para este caso, mas seguindo o requisito.
        raise HTTPException(
            status_code=303,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta_in.cpf}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro ao inserir os dados: {e}")

    return atleta_in


@router.get(
    '/',
    summary='Consultar todos os atletas',
    # Requisito 2 (response) e 4 (paginação)
    response_model=LimitOffsetPage[AtletaListOut],
)
async def get_all_atletas(
    db_session: AsyncSession = Depends(get_session),
    # Requisito 1: Adicionar Query Parameters
    nome: str = Query(None, description="Filtrar por nome do atleta"),
    cpf: str = Query(None, description="Filtrar por CPF do atleta")
):
    query = select(Atleta).join(Categoria).join(CentroTreinamento)
    
    if nome:
        query = query.filter(Atleta.nome == nome)
    if cpf:
        query = query.filter(Atleta.cpf == cpf)
        
    # Requisito 4: Paginação
    return await paginate(db_session, query)