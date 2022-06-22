from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.urls import reverse
User= get_user_model()
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text= models.TextField(max_length=225)
    Author= models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date=models.DateTimeField(auto_now_add=True)
    Published_date=models.DateTimeField(auto_now_add=True)