from django.db import models

# Create your models here.

class Employee(models.Model):
    # Add custom fields for User model

    CATEGORIE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )

    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES, default='D')

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"