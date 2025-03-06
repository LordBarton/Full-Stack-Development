from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm, PizzaForm, DetailsForm, CardForm
from .models import PizzaOrder
from django.contrib.auth.decorators import login_required # only show if user is logged in

# Homepage
def index(request):
    return render(request, 'index.html')

# User Signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# User Login Page
def user_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            request, 
            username=form.cleaned_data['username'], 
            password=form.cleaned_data['password']
        )
        if user:
            login(request, user)
            return redirect('user')
    return render(request, 'login.html', {'form': form})

# Logout, go back home
@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

# Pizza creation view
@login_required
def order_page(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza_order = form.save(commit=False)
            pizza_order.user = request.user  # Assign the logged-in user to the order
            
            # Save the form data to model
            pizza_order.save()

            request.session['order_id'] = pizza_order.id
            return redirect('info')
    else:
        form = PizzaForm()
    
    return render(request, 'order.html', {'form': form})

# create a list of past orders on the user page
@login_required
def order_list(request):
    orders = PizzaOrder.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'user.html', {'orders': orders})

# Ask for delivery and payment information, save the input
@login_required
def info_page(request):
    order = get_object_or_404(PizzaOrder, id=request.session.get('order_id'))

    if request.method == "POST":
        details_form = DetailsForm(request.POST)
        card_form = CardForm(request.POST)

        if details_form.is_valid() and card_form.is_valid():
            # Extract cleaned data only from validated forms
            details_data = details_form.cleaned_data
            card_data = card_form.cleaned_data

            # Assign values
            order.name = details_data['name']
            order.phone_number = details_data['phone_number']
            order.street_address = details_data['street_address']
            order.city = details_data['city']
            order.county = details_data['county']
            order.eire_code = details_data['eire_code']

            order.card_name = card_data['card_name']
            order.card_number = card_data['card_number']
            order.expiry_date = card_data['expiry_date']
            order.card_cvv = card_data['card_cvv']
            
            order.save()
            return redirect('final_page')

    else:
        details_form = DetailsForm()
        card_form = CardForm()

    return render(request, 'info.html', {"details_form": details_form, "card_form": card_form})


# Final order summary page
@login_required
def final_page(request):
    order = get_object_or_404(PizzaOrder, id=request.session.get('order_id'))
    return render(request, 'final_page.html', {"order": order})