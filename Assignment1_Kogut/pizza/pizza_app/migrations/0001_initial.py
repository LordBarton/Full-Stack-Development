# Generated by Django 5.1.5 on 2025-01-29 14:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'), ('xlarge', 'Extra Large')], max_length=20)),
                ('crust', models.CharField(choices=[('normal', 'Normal'), ('thick', 'thin'), ('gluten_free', 'Gluten-Free')], max_length=20)),
                ('sauce', models.CharField(choices=[('tomato', 'Tomato'), ('bbq', 'BBQ'), ('pesto', 'Pesto'), ('garlic', 'Garlic')], max_length=20)),
                ('cheese', models.CharField(choices=[('mozzarella', 'Mozzarella'), ('cheddar', 'Cheddar'), ('vegan', 'Vegan'), ('low_fat', 'Low Fat')], max_length=20)),
                ('other_toppings', models.JSONField(default=list)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
