# schemas.py
from pydantic import BaseModel, Field
from typing import Optional

class CategoriaSchema(BaseModel):
    nome: str

class CentroTreinamentoSchema(BaseModel):
    nome: str

# Requisito 2: Customizar a resposta do GET ALL
class AtletaListOut(BaseModel):
    nome: str
    centro_treinamento: CentroTreinamentoSchema
    categoria: CategoriaSchema

class AtletaIn(BaseModel):
    nome: str = Field(description="Nome do atleta", example="João", max_length=50)
    cpf: str = Field(description="CPF do atleta", example="12345678900", max_length=11)
    idade: int = Field(description="Idade do atleta", example=25)
    peso: float = Field(description="Peso do atleta", example=75.5)
    altura: float = Field(description="Altura do atleta", example=1.70)
    sexo: str = Field(description="Sexo do atleta", example="M", max_length=1)
    categoria: str = Field(description="Nome da categoria", example="Scale")
    centro_treinamento: str = Field(description="Nome do CT", example="CT King")

class AtletaOut(AtletaIn):
    id: int