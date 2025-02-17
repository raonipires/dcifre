import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm.session import Session
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
import os
from dotenv import load_dotenv

load_dotenv()

# Configuração do banco de dados para testes
DATABASE_URL = os.getenv("DATABASE_URL")  # Banco de dados para testes (criar um banco separado para os testes)

# Criação do engine e session local para o banco de dados de teste
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar o banco de dados para testes (sem precisar de conexão ao banco real)
Base.metadata.create_all(bind=engine)

# Configuração do TestClient
client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    # Criação da sessão de testes
    db = SessionLocal()
    yield db
    db.close()

# Teste para a criação de uma empresa
def test_create_empresa(db_session: Session):
    data = {
        "nome": "Empresa Teste",
        "cnpj": "12345678000199",
        "endereco": "Rua Teste, 123",
        "email": "contato@empresa.com",
        "telefone": "123456789",
    }
    
    response = client.post("/empresas/", json=data)
    
    assert response.status_code == 200
    assert response.json()["nome"] == "Empresa Teste"
    assert response.json()["cnpj"] == "12345678000199"

# Teste para listar empresas
def test_get_empresas(db_session: Session):
    response = client.get("/empresas/")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Teste para criação de obrigação acessória
def test_create_obrigacao_acessoria(db_session: Session):
    # Criar a empresa antes de criar a obrigação acessória
    empresa_data = {
        "nome": "Empresa Teste",
        "cnpj": "12345678000199",
        "endereco": "Rua Teste, 123",
        "email": "contato@empresa.com",
        "telefone": "123456789",
    }
    client.post("/empresas/", json=empresa_data)

    # Agora criar a obrigação acessória
    data = {
        "nome": "Declaração de Impostos",
        "periodicidade": "mensal",
        "empresa_id": 1  # Usando o ID da empresa criada
    }

    response = client.post("/obrigacoes_acessorias/", json=data)
    
    assert response.status_code == 200
    assert response.json()["nome"] == "Declaração de Impostos"
    assert response.json()["periodicidade"] == "mensal"

# Teste para listar obrigações acessórias
def test_get_obrigacoes_acessorias(db_session: Session):
    response = client.get("/obrigacoes_acessorias/")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)