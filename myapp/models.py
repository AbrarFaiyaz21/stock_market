from django.db import models

# Create your models here.

class JSONData(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=255)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.CharField(max_length=255)

    def __str__(self):
        return self.trade_code


class SQLData(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=255)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.CharField(max_length=255)

    def __str__(self):
        return self.trade_code