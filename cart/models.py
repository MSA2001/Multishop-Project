from django.db import models

# Create your models here.
from Account.models import User
from Shop.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    size = models.CharField(max_length=3)
    color = models.CharField(max_length=12)
    quantity = models.SmallIntegerField()
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.order.user.phone



