from datetime import date

from django.db import models

from contacts.models import Contact
from warehouse.models import Position

# Create your models here.
class Sale(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Contact, on_delete=models.CASCADE)
    sale_date = models.DateField(default=date.today())
    cost_gross = models.FloatField()
    cost_net = models.FloatField()

    def __str__(self):
        return self.name

class SaleProduct(models.Model):
    product = models.ForeignKey(Position, on_delete=models.CASCADE)
    sale_order = models.ForeignKey(Sale, on_delete=models.CASCADE)