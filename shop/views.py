from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView
from django.db.models import Q
from cart.forms import CartAddProductForm
# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'categories': categories,
        'category': category,
        'products': products,
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Products, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    categoryss = Category.objects.all()
    context = {
        'product': product,
        'form': cart_product_form,
        'categorys': categoryss,
    }
    return render(request, 'shop/product/detail.html', context)


class SearchBox(ListView):
    model = Products
    template_name = 'shop/product/search.html'

    def get_queryset(self):
        query = self.request.GET.get('Q')
        object_list = self.model.objects.filter(Q(name__icontains=query))
        return object_list


def category(request, slug):
    category_posts = Products.objects.filter(category__slug=slug, available=True)
    category_s = Category.objects.filter(slug=slug)
    return render(request, 'shop/category.html', {'slug': slug, 'category_posts': category_posts, 'category_s': category_s})  # noqa

