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
