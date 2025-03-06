from django.db import models
from django.contrib.auth.models import User

class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Cheese(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Sauce(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Crust(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
            return self.name

# Pizza creation model
class PizzaOrder(models.Model):

    # Foreign keys, available options can be added in the admin panel
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    crust = models.ForeignKey(Crust, on_delete=models.SET_NULL, null=True)
    sauce = models.ForeignKey(Sauce, on_delete=models.SET_NULL, null=True)
    cheese = models.ForeignKey(Cheese, on_delete=models.SET_NULL, null=True)

    # for the other toppings checkbox in the pizza form, stores boolean values
    pepperoni = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)
    ham = models.BooleanField(default=False)
    pineapple = models.BooleanField(default=False)
    peppers = models.BooleanField(default=False)
    mushrooms = models.BooleanField(default=False)
    onions = models.BooleanField(default=False)

    # Stores text for the details form
    name = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=20, default="")
    street_address = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    county = models.CharField(max_length=50, default="")
    eire_code = models.CharField(max_length=8, default="")
    
    # Payment form
    card_name = models.CharField(max_length=100, default="")
    card_number = models.CharField(max_length=16, default="")
    expiry_date = models.CharField(max_length=5, default="")
    card_cvv = models.CharField(max_length=3, default="")

    # Stores the date at which the user sumbits the order
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Pizza Order No. {self.id}"
