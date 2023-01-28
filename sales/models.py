from datetime import date

from django.db import models

from contacts.models import Contact
from warehouse.models import Position

# Create your models here.
class Sale(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Contact, on_delete=models.CASCADE)
    sale_date = models.DateField(default=date.today())
    cost_gross = models.FloatField(default=0)
    cost_net = models.FloatField(default=0)

    def save(self):
        if not self.name and self.pk is None:
            last_sale = Sale.objects.all().order_by("-pk").first()
            last_pk = 0
            if last_sale:
                last_pk = last_sale.pk
        
            self.name = "SO-" + str(last_pk+1).zfill(3)

        super(Sale, self).save()

    def __str__(self):
        return self.name

class SaleProduct(models.Model):
    product = models.ForeignKey(Position, on_delete=models.CASCADE)
    sale_order = models.ForeignKey(Sale, on_delete=models.CASCADE)