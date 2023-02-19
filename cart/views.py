from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .cart_module import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from Shop.models import Product
from .models import Order, OrderItem, DiscountCode


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
        messages.success(request, 'product added to cart successfully')
        return redirect('cart:cart_detail')


class CartDeleteView(View):

    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        print(id)
        messages.success(request, 'product removed from cart successfully', 'primary')
        return redirect('cart:cart_detail')


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)

        return render(request, 'cart/order_detail.html', {'order': order})


class OrderCreationView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total())
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], color=item['color'], size=['size'],
                                     quantity=item['quantity'], price=item['price'])

        cart.remove_cart()
        return redirect('cart:order_detail', order.id)


class ApplyDiscountCodeView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        code = request.POST.get('code')
        discount_code = get_object_or_404(DiscountCode, name=code)
        if discount_code.quantity == 0:
            messages.error(request, 'Invalid discount code', 'danger')
            return redirect('cart:order_detail', order.id)

        order.total_price -= order.total_price * discount_code.discount/100
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        messages.success(request, 'Discount code applied successfully', 'success')
        return redirect('cart:order_detail', order.id)
