from django.shortcuts import render
from django.views.decorators.http import require_POST
from .cart import *
from shop.models import *
from django.shortcuts import get_object_or_404, redirect
from .forms import CartAddProductForm
# Create your views here.


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remov(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item["quantity"],
            "override": True
        })
    return render(request, 'cart/detail.html', {'cart': cart})