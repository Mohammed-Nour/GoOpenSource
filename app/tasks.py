from celery import Celery
from .const import CELERY_BROKER_URL
from .mailingsys.mailer import send_mail



app = Celery("tasks", broker=CELERY_BROKER_URL, backend="rpc")


@app.task
def send_email_to_users(email, name):
    subject = "Hello broooooo"
    body = f"Dear {name}, welcom to Go open sourec  "
    send_mail(email, subject, body)
    return "message had  been sent"

@app.task
def send_email_to_multi_user(emails, names):
    
    subject = "Exclusive Preview to Our New Platform's Capabilities"
    count = 6
    for email, name in zip(emails, names):
        if count:
            print(f"hoooo: {email}, Name: {name}")
            count -= 1
            body = f"""Dear {name}, 
I hope this message finds you well. 
We are excited to share with you a significant milestone in our Hackathon.
This email is for testing our Platform for reaching out to our contributors.
Best regards,"""
            send_mail(email, subject, body)
        


