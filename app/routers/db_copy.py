from fastapi import APIRouter ,Depends
from ..cruds.get_db_fields import get_repository_fields,get_contributor_fields,get_contributor_repository_fields
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter()

@router.get("/get/Repo_fildes")
def read_items(db: Session = Depends(get_db)):
    return get_repository_fields(db)

@router.get("/get/Contributor_fields")
def read_contributors(db: Session = Depends(get_db)):
    return get_contributor_fields(db)

@router.get("/get/ContributorRepository_fields")
def read_contributor_repository(db: Session = Depends(get_db)):
    return get_contributor_repository_fields(db)