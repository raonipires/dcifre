from database import engine, Base
from models import Empresa, ObrigacaoAcessoria 
from sqlalchemy import inspect

# Criar as tabelas no banco de dados
try:
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")
except Exception as e:
    print(f"Erro ao criar tabelas: {e}")

# Testar se há tabelas no banco
inspector = inspect(engine)
tables = inspector.get_table_names()

if tables:
    print("Tabelas encontradas:", tables)
else:
    print("Nenhuma tabela foi criada!")