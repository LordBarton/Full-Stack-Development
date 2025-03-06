from django.contrib import admin
from .models import PizzaOrder, Size, Cheese, Sauce, Crust

# Registered the pizza creation model 
# to access the order data table through the admin panel
admin.site.register(PizzaOrder)
admin.site.register(Size)
admin.site.register(Cheese)
admin.site.register(Sauce)
admin.site.register(Crust)