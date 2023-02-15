# Generated by Django 4.1 on 2023-02-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='Shop.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='Shop.size'),
        ),
    ]