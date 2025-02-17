import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Pegar a URL do banco de dados do .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Criar a engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Criar sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# Teste de conecção com o banco de dados
try:
    with engine.connect() as connection:
        print("Conexão estabelecida com sucesso!")
except Exception as e:
    print(f"Erro ao conectar: {e}")