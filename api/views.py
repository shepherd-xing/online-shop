from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_extensions.mixins import NestedViewSetMixin
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, OrderSerializer,\
    OrderItemSerializer
from shop.models import Category, Product
from cart.models import CartModel
from orders.models import Order, OrderItem

# Create your views here.

class CategoryViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ProductViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class CartViewSet(ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

class OrderViewSet(NestedViewSetMixin, ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

class OrderItemViewSet(NestedViewSetMixin, ReadOnlyModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated,)