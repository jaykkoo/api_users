from django.db import models

# Create your models here.

class Region(models.Model):
    # Add custom fields for User model

    region = models.CharField(max_length=40, default='')

    user = models.OneToOneField('user.Employee', on_delete=models.CASCADE)