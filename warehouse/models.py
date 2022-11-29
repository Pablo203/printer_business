from django.db import models

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

class Position(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    color = models.CharField(max_length=100, default='')
    filamentType = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    manufacturer = models.CharField(max_length=100, default='')
    pathToImg = models.CharField(max_length=150, default='#')

    def __str__(self):
        return self.name