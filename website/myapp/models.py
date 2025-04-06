from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.text import slugify
# Create your models here.

class CustomUser(AbstractUser):
    mobile=models.CharField(max_length=10)
    city_town_village = models.CharField(max_length=100 , blank=True, null=True , verbose_name="City/Town/Village")
    street_name = models.CharField(max_length=255 , blank=True, null=True )
    pin_code = models.CharField(max_length=6 , blank=True, null=True)
    

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('AC Repair', 'AC Repair'),
        ('Fridge Repair', 'Fridge Repair'),
        ('Maintenance', 'Maintenance'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    booking_date = models.DateField()
    message = models.TextField(blank=True, null=True)
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} on {self.booking_date}"    
    
 
class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='service_images/')
    
    
    def __str__(self):
        return self.name


