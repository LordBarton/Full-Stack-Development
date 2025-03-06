from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PizzaOrder, Size, Crust, Sauce, Cheese
import datetime

# Simple Sign up nad login forms
class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# the Pizza creation form connected to the pizzaorder model
class PizzaForm(forms.ModelForm):
    # Takes options from the model, modifiable in the admin panel
    size = forms.ModelChoiceField(queryset=Size.objects.all(), empty_label="Select Size", required=True)
    crust = forms.ModelChoiceField(queryset=Crust.objects.all(), empty_label="Select Crust", required=True)
    sauce = forms.ModelChoiceField(queryset=Sauce.objects.all(), empty_label="Select Sauce", required=True)
    cheese = forms.ModelChoiceField(queryset=Cheese.objects.all(), empty_label="Select Cheese", required=True)

    class Meta:
        model = PizzaOrder
        fields = [
            'size', 'crust', 'sauce', 'cheese',
            'pepperoni', 'chicken', 'ham', 'pineapple',
            'peppers', 'mushrooms', 'onions'
        ]

# Delivery details form, gets saved in the pizzaorder model
class DetailsForm(forms.ModelForm):

    class Meta:
        model = PizzaOrder
        fields = ['name', 'phone_number', 'street_address', 'city', 'county', 'eire_code']
        
        # County options for the dropdown box
        widgets = {
            'county': forms.Select(choices=[
                ('', 'Select County'),
                ('D', 'Dublin'),
                ('CK', 'Cork'),
                ('GY', 'Galway'),
                ('CE', 'Clare'),
                ('KY', 'Kerry'),
                ('KE', 'Kildare'),
                ('LK', 'Limerick'),
                ('LH', 'Louth'),
                ('MO', 'Mayo'),
                ('MH', 'Meath'),
                ('WD', 'Waterford'),
            ])
        }

# Payment details form, also gets saved with the user's order model
class CardForm(forms.ModelForm):

    class Meta:
        model = PizzaOrder
        fields = ['card_name', 'card_number', 'expiry_date', 'card_cvv']
        widgets = {
            'expiry_date': forms.TextInput(attrs={'placeholder': 'MM/YY'}),
            'card_number': forms.TextInput(attrs={'placeholder': 'Enter 16-digit card number, no spaces'}),
            'card_cvv': forms.TextInput(attrs={'placeholder': 'Enter 3-digit CVV'}),

        }

    # Validate the name input 
    def clean_card_name(self):
        card_name = self.cleaned_data['card_name']
        if card_name.isdigit():
            raise forms.ValidationError("Cardholder's name must contain only letters.")
        return card_name
    
    # Validate the card number input
    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        if not card_number.isdigit():
            raise forms.ValidationError("Card number must contain only digits.")
        elif len(str(card_number)) != 16:
            raise forms.ValidationError("Card number must be 16 digits long.")
        
        return card_number

    # Validate card expiry date input
    def clean_expiry_date(self):
        expiry_date = self.cleaned_data['expiry_date']
        today = datetime.date.today()

        try:
            # Extract the date from the formatted input
            split = expiry_date.split('/')
            month = int(split[0])
            year = int(split[1])
            expiry = datetime.date(year=2000+year, month=month, day=1)
        except ValueError:
            # If the format used wasn't correct, raise error
            raise forms.ValidationError("Enter expiry date in MM/YY format.")

        # Compare to today's date, if it's expired raise error
        if expiry < today:
            raise forms.ValidationError("The card has expired.")
        
        return expiry_date

    # Validate cvv
    def clean_card_cvv(self):
        card_cvv = self.cleaned_data['card_cvv']
        
        # Check if the code is digits only
        if not card_cvv.isdigit():
            raise forms.ValidationError("Card CVV must contain only digits.")
        elif len(str(card_cvv)) != 3:
            raise forms.ValidationError("Card CVV must be 3 digits long.")
        
        return card_cvv