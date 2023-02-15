from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import DetailView

from Shop.models import Product


def home(request):
    return render(request, 'Shop/index.html')


class ProductDetailView(DetailView):
    template_name = 'Shop/detail.html'
    model = Product
    