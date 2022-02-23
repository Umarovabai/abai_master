from django.core.mail import send_mail

from cinema.celery import app

@app.task
def notify_user(email):
    send_mail('Вы создали новый запрос!',
              'Спасибо за исполдзование нашего сайта!',
              'test@gmail.com',
              [email])

    return 'Success'