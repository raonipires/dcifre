from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal

app = FastAPI()

# Dependência para injetar o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "API Ok"}

@app.post("/empresas/", response_model=schemas.EmpresaRead)
def criar_empresa(empresa: schemas.EmpresaBase, db: Session = Depends(get_db)):
    return crud.criar_empresa(db, empresa)

@app.get("/empresas/", response_model=list[schemas.EmpresaRead])
def listar_empresas(db: Session = Depends(get_db)):
    return crud.obter_empresas(db)

@app.get("/empresas/{empresa_id}", response_model=schemas.EmpresaDetalhada)
def obter_empresa(empresa_id: int, db: Session = Depends(get_db)):
    empresa = crud.obter_empresa_por_id(db, empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

@app.put("/empresas/{empresa_id}", response_model=schemas.EmpresaRead)
def atualizar_empresa(empresa_id: int, empresa: schemas.EmpresaBase, db: Session = Depends(get_db)):
    return crud.atualizar_empresa(db, empresa_id, empresa)

@app.delete("/empresas/{empresa_id}")
def deletar_empresa(empresa_id: int, db: Session = Depends(get_db)):
    return crud.deletar_empresa(db, empresa_id)

@app.post("/obrigacoes/", response_model=schemas.ObrigacaoAcessoriaRead)
def criar_obrigacao(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    return crud.criar_obrigacao(db, obrigacao)

@app.get("/obrigacoes/{empresa_id}", response_model=list[schemas.ObrigacaoAcessoriaRead])
def listar_obrigacoes(empresa_id: int, db: Session = Depends(get_db)):
    return crud.obter_obrigacoes(db, empresa_id)