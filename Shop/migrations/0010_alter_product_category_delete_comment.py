# Generated by Django 4.1 on 2023-02-20 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='Shop.category'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
