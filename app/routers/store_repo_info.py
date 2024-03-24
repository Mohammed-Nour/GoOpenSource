from fastapi import APIRouter ,Depends ,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..cruds.save_gh import store_repo_info 
import requests
from ..cruds.get_db_fields import get_contributor_fields,get_contributor_repository_fields,get_repository_fields 
from ..tasks import send_email_to_multi_user
from ..cruds.save_gh import extract_contributor_and_emails
router = APIRouter()

@router.get('/store_data')
def store_info(db: Session = Depends(get_db)):
    stored_result = store_repo_info(db)
    repository_fields = get_repository_fields(db)
    contributor_fields = get_contributor_fields(db)
    contributor_repository_fields = get_contributor_repository_fields(db)
    # response_1 = requests.post('http://91.107.124.108:5173/v1/repositories', json=repository_fields)
    # response_2 = requests.post('http://91.107.124.108:5173/v1/contributors', json=contributor_fields)
    # response_3 = requests.post('http://91.107.124.108:5173/v1/contributorRepositories', json=contributor_repository_fields)
    emails,names=extract_contributor_and_emails()
    print(emails,names)
    send_email_to_multi_user.delay(emails,names)
    # if response_3.status_code == 201:
    #     return {"message": "Data sent successfully"}
    # else:
    #     raise HTTPException(status_code=response_3.status_code, detail="Failed to send data to external endpoint")

