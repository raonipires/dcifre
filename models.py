from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Tabela empresas
class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    endereco = Column(String)
    email = Column(String)
    telefone = Column(String)

    obrigacoes_acessorias = relationship("ObrigacaoAcessoria", back_populates="empresa")

#tabela obrigações acessoria
class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacoes_acessorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    periodicidade = Column(String, nullable=False)  # Pode ser mensal, trimestral ou anual
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)

    empresa = relationship("Empresa", back_populates="obrigacoes_acessorias")