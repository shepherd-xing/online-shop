from rest_framework.serializers import ModelSerializer, CharField
from shop.models import Category, Product
from cart.models import CartModel
from orders.models import Order, OrderItem

class ProductSerializer(ModelSerializer):
    category = CharField(source='category.name')
    class Meta:
        model = Product
        exclude = ('slug',)

class CategorySerializer(ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'products')

class CartSerializer(ModelSerializer):
    product_name = CharField(source='product.name')
    class Meta:
        model = CartModel
        fields = ('id', 'product_name', 'quantity', 'added', 'update')

class OrderItemSerializer(ModelSerializer):
    product_name = CharField(source='product.name')
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product_name', 'price', 'quantity')

class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'




