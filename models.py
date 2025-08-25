# models.py
from sqlalchemy import Integer, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column

Base = declarative_base()

class Atleta(Base):
    __tablename__ = 'atletas'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer)
    peso: Mapped[float] = mapped_column(Float)
    altura: Mapped[float] = mapped_column(Float)
    sexo: Mapped[str] = mapped_column(String(1))
    
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))
    categoria: Mapped["Categoria"] = relationship(back_populates="atletas")

    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey("centros_treinamento.id"))
    centro_treinamento: Mapped["CentroTreinamento"] = relationship(back_populates="atletas")

class Categoria(Base):
    __tablename__ = 'categorias'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    atletas: Mapped[list["Atleta"]] = relationship(back_populates="categoria")

class CentroTreinamento(Base):
    __tablename__ = 'centros_treinamento'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60))
    proprietario: Mapped[str] = mapped_column(String(30))
    atletas: Mapped[list["Atleta"]] = relationship(back_populates="centro_treinamento")