from sqlalchemy.orm import Session
from models import Empresa, ObrigacaoAcessoria
import schemas

# Criar Empresa
def criar_empresa(db: Session, empresa_data: schemas.EmpresaCreate):
    nova_empresa = Empresa(**empresa_data.model_dump())
    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)
    return nova_empresa

# Obter todas as empresas
def obter_empresas(db: Session):
    return db.query(Empresa).all()

# Obter empresa por ID
def obter_empresa_por_id(db: Session, empresa_id: int):
    return db.query(Empresa).filter(Empresa.id == empresa_id).first()

# Atualizar empresa
def atualizar_empresa(db: Session, empresa_id: int, empresa_data: schemas.EmpresaCreate):
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if empresa:
        for key, value in empresa_data.model_dump().items():
            setattr(empresa, key, value)
        db.commit()
        db.refresh(empresa)
    return empresa

# Deletar empresa
def deletar_empresa(db: Session, empresa_id: int):
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if empresa:
        db.delete(empresa)
        db.commit()
    return empresa

# Criar Obrigação Acessória
def criar_obrigacao(db: Session, obrigacao_data: schemas.ObrigacaoAcessoriaCreate):
    nova_obrigacao = ObrigacaoAcessoria(**obrigacao_data.model_dump())
    db.add(nova_obrigacao)
    db.commit()
    db.refresh(nova_obrigacao)
    return nova_obrigacao

# Atualizar Obrigação Acessória
def atualizar_obrigacao(db: Session, obrigacao_id: int, obrigacao_data: schemas.ObrigacaoAcessoriaCreate):
    obrigacao = db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()
    if obrigacao:
        for key, value in obrigacao_data.model_dump().items():
            setattr(obrigacao, key, value)
        db.commit()
        db.refresh(obrigacao)
    return obrigacao

# Deletar Obrigação Acessória
def deletar_obrigacao(db: Session, obrigacao_id: int):
    obrigacao = db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()
    if obrigacao:
        db.delete(obrigacao)
        db.commit()
    return obrigacao

# Obter todas as obrigações por empresa
def obter_obrigacoes(db: Session, empresa_id: int):
    return db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.empresa_id == empresa_id).all()