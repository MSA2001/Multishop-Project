# Generated by Django 4.1 on 2023-02-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_order_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('discount', models.SmallIntegerField(default=0)),
                ('quantity', models.SmallIntegerField(default=1)),
            ],
        ),
    ]