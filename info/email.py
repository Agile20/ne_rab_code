from django.core.mail import EmailMessage

from django.conf import settings

from celery import shared_task

@shared_task
def message(email):
    mail = EmailMessage(
        'Hello',
        'Ваша заявка была принята и проходит проверку :)',
        settings.EMAIL_HOST_USER,
        [email]        
    )
    mail.send()
