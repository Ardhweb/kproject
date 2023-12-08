from django.db import models

# Create your models here.
from django.conf import settings
HOBBIES_CHOICES = ( 
    ("Movies", "Movies"), 
    ("Games", "Games"), 
    ("Books", "Books"), 
) 

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='users/%Y/%m/dp/',blank=True)
    full_name =models.CharField( max_length=50, default="")
    email = models.EmailField( max_length=250, default="")
    bio  = models.CharField( max_length=50,blank=True)
    hobby = models.CharField(max_length=50,blank=True,choices=HOBBIES_CHOICES)
    
    def __str__(self):
        return f'Profile for user {self.user.username}'