from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .cart_module import Cart

# Create your views here.
from Shop.models import Product


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart_detail.html', {'cart': cart})


class CartAddView(View):

    def post(self, request, pk):
        size, color, quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('quantity')
        product = get_object_or_404(Product, id=pk)
        cart = Cart(request)
        cart.add(product, quantity, color, size)
        print(size, color, quantity)
        return redirect('cart:cart_detail')
