from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    department = models.CharField(max_length=255)
    purpose = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    unit = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name