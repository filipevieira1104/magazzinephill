from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order

@shared_task
def payment_completed(order_id):
    """
    Tarefa para enviar uma notificação por e-mail quando um pedido for
    pago com sucesso.
    """
    order = Order.objects.get(id=order_id)
    # criar e-mail de fatura
    subject = f'MagazzinePhill - nº do pedido {order.id}'
    message = 'Sua nota fiscal foi emitida.'
    email = EmailMessage(subject,
                         message,
                         'marketplacefea@outlook.com',
                         [order.email])
    # gerar PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out,
                                          stylesheets=stylesheets)
    # anexar arquivo PDF
    email.attach(f'order_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')
    # enviar email
    email.send()