from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY_CHOICES = (
    ('GC', 'Gaming Consoles'), 
    ('GL', 'Gaming Laptops/PCs'), 
    ('GMK', 'Gaming Mouse'),
    ('GK', 'Gaming Keyboards'), 
    ('GH', 'Gaming Headsets'), 
    ('GM', 'Gaming Monitors'), 
    ('GCH', 'Gaming Chairs'), 
) 

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=4)  # Adjusted max_length to 4
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name  # Fixed the incorrect field reference

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.TextField()
    city = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)  # Corrected to CharField to store phone numbers as text
    
    def __str__(self):
        return self.name