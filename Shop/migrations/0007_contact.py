# Generated by Django 4.1 on 2023-02-20 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_alter_product_color_alter_product_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=600)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
