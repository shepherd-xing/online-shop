from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()
categories_router = router.register('categories', views.CategoryViewSet, base_name='categories')
categories_router.register('products', views.ProductViewSet, base_name='products',
                           parents_query_lookups=['category'])
router.register('cart', views.CartViewSet, base_name='cart')
order_router = router.register('order', views.OrderViewSet, base_name='order')
order_router.register('order_item', views.OrderItemViewSet, base_name='order_item',
                      parents_query_lookups=['order'])

urlpatterns = router.urls

