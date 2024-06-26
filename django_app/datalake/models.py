from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    password = models.TextField()
