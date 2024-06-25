from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order number of: {order.id}'
    message = (f'Welcome {order.first_name},\n\n'
               f'You placed order in our shop :)\n'
               f'ID your order: {order.id}.')
    mail_sent = send_mail(subject, message, "admin@myshop.com", [order.email])
    return mail_sent
