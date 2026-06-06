from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
# Relational Databases -> Tables

class Post(models.Model):
    title = models.CharField(max_length=100) #string
    subtitle = models.CharField(max_length=100) #string
    body = models.TextField() #string
    created_on = models.DateTimeField(auto_now_add=True) #datetime
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )#string / object
    
    
    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        # automatically redirects to the detail page of the post after creating a new post
        return reverse("post_detail", args=[str(self.id)])