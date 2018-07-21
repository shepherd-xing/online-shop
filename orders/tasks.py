from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = '{}, \n\n您已成功下单。您的订单编号是{}。'.formate(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'shepherd-xing@outlook.com', [order.email])
    return mail_sent