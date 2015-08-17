from django.db import models

# Create your models here.

class Customers(models.Model):
    cust_id = models.IntegerField(primary_key=True)
    cust_name = models.CharField(max_length=42)
    phone = models.IntegerField()
    email = models.CharField(max_length=42)
    address = models.CharField(max_length=128)

class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=42)

class Products(models.Model):
    prod_id = models.IntegerField(primary_key=True)
    prod_name = models.CharField(max_length=128)
    cat_id = models.ForeignKey('Category')
    buying_price = models.IntegerField()
    selling_price = models.IntegerField()

class Orders(models.Model):
    sno = models.IntegerField()
    order_id = models.CharField(max_length=128, primary_key=True)
    cust_id = models.CharField(max_length=128)
    order_buyingprice = models.IntegerField()
    order_sellingprice = models.IntegerField()
    timestamp = models.DateTimeField()

class Orderdetails(models.Model):
    sno = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey('Orders')
    buying_price = models.IntegerField()
    selling_price = models.IntegerField()
    prod_id = models.ForeignKey('Products')
    quantity = models.IntegerField()
    order_completed = models.NullBooleanField()
    
    
class Prices(models.Model):
    price_id = models.IntegerField(primary_key=True)
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
    vendor_id = models.IntegerField(primary_key=True)
    vendor_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.IntegerField()
    email = models.EmailField()
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
    measurement = models.CharField(max_length=128)
    used_quantity = models.IntegerField()
    timestamp = models.DateTimeField()

class Dailyexpenses(models.Model):
    sno = models.IntegerField()
    product = models.CharField(max_length=100)
    purchased_at = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField()
    vendor_id = models.ForeignKey('Vendors')
