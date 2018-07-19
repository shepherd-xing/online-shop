from django.db import models
from shop.models import Product

# Create your models here.
class Order(models.Model):
    '''订单信息，比如收货人姓名地址等'''
    first_name = models.CharField('名', max_length=50)
    last_name = models.CharField('姓', max_length=50)
    email = models.EmailField('邮箱')
    address = models.CharField('地址', max_length=250)
    postal_code = models.CharField('邮编', max_length=6)
    city=models.CharField('城市', max_length=100)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('修改时间', auto_now=True)
    paid = models.BooleanField('是否付款', default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '订单编号：{}'.format(self.id)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    '''订单中的商品的信息，相同商品为一条信息，也是一个OrderItem实例'''
    order = models.ForeignKey(Order, verbose_name='所在订单', related_name='items')
    product = models.ForeignKey(Product, verbose_name='商品', related_name='order_items')
    price = models.DecimalField('价格', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('数量', default=1)

    def __str__(self):
        return 'OrderItem编号：{}'.formate(self.id)
    def get_cost(self):
        return self.price * self.quantity















