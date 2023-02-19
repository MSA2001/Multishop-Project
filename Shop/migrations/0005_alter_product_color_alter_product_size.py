# Generated by Django 4.1 on 2023-02-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_alter_product_color_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='products', to='Shop.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='products', to='Shop.size'),
        ),
    ]
