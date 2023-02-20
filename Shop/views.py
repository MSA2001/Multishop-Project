from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import DetailView
from .forms import ContactForm
from Shop.models import Product, Contact


def home(request):
    return render(request, 'Shop/index.html')


class ProductDetailView(DetailView):
    template_name = 'Shop/detail.html'
    model = Product


class ContactView(View):
    form_class = ContactForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'Shop/contact.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Contact.objects.create(name=cd['name'], email=cd['email'], title=cd['title'], text=cd['text'])
            messages.success(request, 'You sent a message successfully.', 'success')
            return redirect('shop:home')
        else:
            messages.error(request, 'failed to sent a message, try again.')
            return redirect('shop:contact_us')

        return render(request, 'Shop/contact.html', {'form': form})


class ShopView(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'Shop/shop.html', {'products': products})


class CategoryDetailView(View):

    def get(self, request, pk):
        products = Product.objects.filter(category=pk)
        return render(request, 'Shop/shop.html', {'products': products})
