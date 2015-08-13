from django.db import models

# Create your models here.

class Prices(models.Model):
    price_id = models.IntegerField()
    product = models.CharField(max_length=200)
    quantity = models.IntegerField()
    measurement = models.CharField(max_length=20)
    buying_price = models.IntegerField()
    price_per = models.IntegerField()
    local_price = models.IntegerField()
    online_price = models.IntegerField()
    selling_price = models.IntegerField()
    profit = models.IntegerField()

class Vendors(models.Model):
    vendor_id = models.IntegerField()
    vendor_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    tin = models.CharField(max_length=20)
    account = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=11)
    category = models.CharField(max_length=50)

class Stock(models.Model):
    sno = models.IntegerField()
    product = models.CharField(max_length=100)
    category  = models.CharField(max_length=100)
    stock = models.IntegerField()
    used_quantity = models.IntegerField()

class Dailyexpenses(models.Model):
    sno = models.IntegerField()
    product = models.CharField(max_length=100)
    purchased_at = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField()
