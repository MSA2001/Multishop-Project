from django.urls import path
from . import views

app_name = 'shop'


urlpatterns = [
    path('', views.home, name='home'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('contact/', views.ContactView.as_view(), name='contact_us'),
    path('shop/', views.ShopView.as_view(), name='shop'),
]