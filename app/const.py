import os

CELERY_BROKER_URL = os.getenv(
    "CELERY_BROKER_URL", "amqp://GoOpenSource:GoOpenSource2024@localhost:5672/GOS"
)
MAIL_HOST = os.getenv("MAIL_HOST", "smtp.gmail.com")
MAIL_USERNAME = os.getenv("MAIL_USERNAME", "saleemasekrea000@gmail.com")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "jguhugxjgwwkpuhe")
MAIL_PORT = os.getenv("MAIL_PORT", "587")