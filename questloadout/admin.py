from django.contrib import admin
from .models import Product, Customer
from .forms import CustomerProfileForm  # Import the form, if needed

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'image', 'category']
    list_filter = ['category', 'price']
    search_fields = ['name', 'description']
    list_editable = ['price', 'category']
    ordering = ['id']

# Register the Customer model with a ModelAdmin
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'locality', 'city', 'mobile']  # Adjust this based on your Customer model fields
    search_fields = ['name', 'locality', 'city', 'mobile']
    list_filter = ['city']  # Add more filters if needed


