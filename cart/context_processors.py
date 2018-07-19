from .cart import Cart
from .models import CartModel

def cart(request):
    if request.user.is_authenticated():
        cart_list = CartModel.objects.filter(user=request.user)
        total_cost = sum(cart_.get_total_price() for cart_ in cart_list)
        return {'cart_list':cart_list, 'total_cost':total_cost}
    else:
        return {'cart': Cart(request)}