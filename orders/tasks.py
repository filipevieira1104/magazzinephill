from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from django.http import HttpResponse

@shared_task
def order_created(order_id):
    """
    Tarefa para enviar uma notificação por e-mail quando um pedido for
    criado com sucesso.
    """
    order = Order.objects.get(id=order_id)
    subject = f'pedido nr. {order.id}'
    message = f'Querido {order.first_name},\n\n' \
              f'Você fez um pedido com sucesso.' \
              f'O número do seu pedido é {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'marketplacefea@outlook.com',
                          [order.email])

    return mail_sent