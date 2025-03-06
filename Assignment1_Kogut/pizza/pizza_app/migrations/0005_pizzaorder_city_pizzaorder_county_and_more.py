# Generated by Django 5.1.5 on 2025-02-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0004_cheese_crust_sauce_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzaorder',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='county',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='eire_code',
            field=models.CharField(default='', max_length=9),
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='street_address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
