from django.db import models



# Create your models here.

class Requester (models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self)   :
        return self.name
    

# models.py

class PurchaseRequestItem(models.Model):
    department = models.CharField(max_length=100)
    purpose = models.TextField()
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    item_unit = models.CharField(max_length=50)
    item_quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self)   :
        return self.item_name