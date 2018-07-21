from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm, CartForm
from .models import CartModel

# Create your views here.

@require_POST
def cart_add(request, product_id):
    if request.user.is_authenticated():
        quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart_set = CartModel.objects.filter(user=request.user).values()
        id_list = []
        for item in cart_set:
            id_list.append(item['product_id'])
        if int(product_id) in id_list:
            cart = CartModel.objects.get(product=product)
            cart.quantity = cart.quantity + quantity
        else:
            cart = CartModel()
            cart.user = request.user
            cart.product = product
            cart.quantity = quantity
        cart.save()

    else:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    if request.user.is_authenticated():
        product = get_object_or_404(Product, id=product_id)
        cart = CartModel.objects.get(product=product)
        cart.delete()

    else:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
    return redirect('cart:cart_detail')
def cart_detail(request):
    if request.user.is_authenticated():
        cart_list = CartModel.objects.filter(user=request.user)
        if request.method == 'POST':
            product_id = request.POST.get('p_id')
            quantity = int(request.POST.get('quantity'))
            product = get_object_or_404(Product, id=product_id)
            cart = get_object_or_404(CartModel, product=product)
            form = CartForm(request.POST)
            if form.is_valid():
                cart.quantity = quantity
                cart.save()
        else:
            form = CartForm()
        total_cost = sum(cart.get_total_price() for cart in cart_list)
        context = {'form': form, 'total_cost': total_cost}
        return render(request, 'cart/cart_detail.html', context)
    else:
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                initial={'quantity':item['quantity'], 'update':True})
        return render(request, 'cart/detail.html', {'cart':cart})












