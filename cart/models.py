from django.db import models
from django.conf import settings

# Create your models here.
class CartModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_cart')
    product = models.ForeignKey('shop.Product')
    quantity = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    update = models.BooleanField('修改数量', default=False)
    class Meta:
        ordering = ('-added',)

    def get_total_price(self):
        total = self.product.price * self.quantity
        return total


