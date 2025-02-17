from pydantic import BaseModel, Field
from typing import List, Optional

# Schema para criação de empresa (entrada)
class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

    class Config:
        json_schema_extra = {
            "example": {
                "nome": "Empresa Teste",
                "cnpj": "12345678000199",
                "endereco": "Rua Teste, 123",
                "email": "contato@empresa.com",
                "telefone": "123456789",
            }
        }

# Schema para leitura de empresa (saída)
class EmpresaRead(EmpresaBase):
    id: int

    class Config:
        from_attributes = True  # Garante compatibilidade com SQLAlchemy

# Schema para criação de obrigação acessória (entrada)
class ObrigacaoAcessoriaCreate(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

    class Config:
        json_schema_extra = {
            "example": {
                "nome": "ABC",
                "periodicidade": "mensal",
            }
        }

# Schema para leitura de obrigação acessória (saída)
class ObrigacaoAcessoriaRead(ObrigacaoAcessoriaCreate):
    id: int

    class Config:
        from_attributes = True

# Schema para listar empresa com suas obrigações (saída detalhada)
class EmpresaDetalhada(EmpresaRead):
    obrigacoes_acessorias: List[ObrigacaoAcessoriaRead] = []