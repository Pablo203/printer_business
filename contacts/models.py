from django.db import models
from phone_field import PhoneField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=15, default='')
    photoPath = models.CharField(max_length=100, default='/static/contacts/no-user-photo.png')
    
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.name