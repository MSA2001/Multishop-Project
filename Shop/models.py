from django.db import models

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='subs')
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Size(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category, related_name='products', null=True, blank=True)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='products')
    size = models.ManyToManyField(Size, related_name='products', null=True, blank=True)
    color = models.ManyToManyField(Color, related_name='products', null=True, blank=True)

    def __str__(self):
        return self.title


class Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='information')
    text = models.TextField()

    def __str__(self):
        return self.text[:35]


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
