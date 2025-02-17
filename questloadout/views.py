from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User  
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Customer
from .forms import RegistrationForm, LoginForm, CustomerProfileForm

# Home Page View
def home(request):
    return render(request, 'quest/home.html')

# About Page View
def about(request):
    return render(request, 'quest/about.html')

# Contact Page View
def contact(request):
    return render(request, 'quest/contact.html')

# Category View
class CategoryView(View):
    def get(self, request, val):
        products = Product.objects.filter(category=val)
        return render(request, 'quest/category.html', {'products': products, 'category': val})

# Product Detail View
class ProductDetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'quest/productdetail.html', {'product': product})

# Registration View
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if user already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken!")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered!")
            else:
                # Create user
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, "quest/register.html", {'form': form})

# Login View
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')  # Redirect to home or dashboard after successful login
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "quest/login.html", {'form': form})

# Logout View
def custom_logout(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('home')

# Profile View

class ProfileView(View):
    def get(self, request):
        user_form = None
        form = None
        customer_data = None
        all_customers = None  # Store all customers for the superuser

        if request.user.is_superuser:
            # Fetch all customers for superuser to manage
            all_customers = Customer.objects.all()
            user_id = request.GET.get('user_id')

            if user_id:
                # If a user ID is provided, load that customer's data for editing
                customer = get_object_or_404(Customer, user_id=user_id)
                form = CustomerProfileForm(instance=customer)
                customer_data = customer
            else:
                # If no specific user is selected, provide empty forms for adding a new customer
                form = CustomerProfileForm()
                user_form = UserCreationForm()
        else:
            # Normal user: View and update only their own profile
            customer, created = Customer.objects.get_or_create(user=request.user)
            form = CustomerProfileForm(instance=customer)
            customer_data = customer

        return render(request, "quest/profile.html", {
            'form': form,
            'user_form': user_form,
            'customer_data': customer_data,
            'is_superuser': request.user.is_superuser,
            'all_customers': all_customers  # List of all customers for superuser management
        })

    def post(self, request):
        user_form = None
        customer_data = None

        if request.user.is_superuser:
            user_id = request.POST.get('user_id')

            if user_id:
                # Superuser updating an existing customer
                customer = get_object_or_404(Customer, user_id=user_id)
                form = CustomerProfileForm(request.POST, instance=customer)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Customer profile updated successfully.")
                    return redirect('profile')
                customer_data = customer
            else:
                # Superuser adding a new customer
                user_form = UserCreationForm(request.POST)
                form = CustomerProfileForm(request.POST)
                if user_form.is_valid() and form.is_valid():
                    new_user = user_form.save()
                    customer = form.save(commit=False)
                    customer.user = new_user
                    customer.save()
                    messages.success(request, "New customer added successfully.")
                    return redirect('profile')
                customer_data = None
        else:
            # Normal user updating their own profile
            customer, created = Customer.objects.get_or_create(user=request.user)
            form = CustomerProfileForm(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully.")
                return redirect('profile')
            customer_data = customer

        # Fetch all customers again for superuser view
        all_customers = Customer.objects.all() if request.user.is_superuser else None

        return render(request, "quest/profile.html", {
            'form': form,
            'user_form': user_form,
            'customer_data': customer_data,
            'is_superuser': request.user.is_superuser,
            'all_customers': all_customers
        })