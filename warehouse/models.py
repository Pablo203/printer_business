from django.db import models
from contacts.models import Contact

# Create your models here.
class MainCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    topCategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CategoryValue(models.Model):
    propertyName = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    

    def __str__(self):
        return self.propertyName

class Position(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    imagePath = models.CharField(max_length=200, default='/static/positionImgs/no-image.png')
    amount = models.IntegerField(default=0)
    data = models.JSONField(default=dict)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    vendor = models.ForeignKey(Contact, on_delete=models.CASCADE)
    product = models.ForeignKey(Position, on_delete=models.CASCADE)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.vendor.name