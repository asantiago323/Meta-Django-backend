from django.db import models

# Create your models here.
class menu(models.Model):
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f"{self.item}: {str(self.price)}"

class booking(models.Model):
    tableno = models.IntegerField()
    persons = models.IntegerField()