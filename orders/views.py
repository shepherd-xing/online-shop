from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from cart.models import CartModel

# Create your views here.

def order_create(request):
    if request.user.is_authenticated():
        cart_list = CartModel.objects.filter(user=request.user)
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for cart in cart_list:
                    OrderItem.objects.create(order=order, product=cart.product, price=cart.product.price,
                                             quantity=cart.quantity)
                    cart.delete()

                return render(request, 'orders/order/created.html', {'order': order})
        else:
            form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'form': form})

    else:
        cart = Cart(request)
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                             quantity=item['quantity'])

                cart.clear()
                return render(request, 'orders/order/created.html', {'order':order})
        else:
            form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'cart':cart, 'form':form})




















