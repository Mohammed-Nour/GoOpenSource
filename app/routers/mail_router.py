
from fastapi import APIRouter
from ..tasks import send_email_to_users , send_email_to_multi_user
router = APIRouter()


@router.post("/send-email")
def send_email(email: str, name: str ):
    send_email_to_users.delay(email,name)


@router.post("/send-multiple-emails")
def send_multiple_emails(emails: list[str], names: list[str]):
    send_email_to_multi_user.delay(emails,names)


