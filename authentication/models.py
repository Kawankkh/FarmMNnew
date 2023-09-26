from django.db import models

# Create your models here.
class Custormer(models.Model):
    custormer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_contact = models.CharField(max_length=255)
    def __str__(self):
        return self.customer_name
class Farmer(models.Model):
    Farmer_id = models.AutoField(primary_key=True)
    Farmer_name = models.CharField(max_length=255)
    Farmer_contact = models.CharField(max_length=255)
    def __str__(self):
        return self.Farmer_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_description = models.CharField(max_length=255)
    product_price = models.FloatField()
    def __str__(self):
        return self.product_description 
class Bill_OP(models.Model):
    Bill_id = models.AutoField(primary_key=True)
    Farmer =models.ForeignKey(Farmer,on_delete=models.CASCADE)
    Pay_status =  models.BooleanField(default=False)
    billdate =  models.DateTimeField()
    def __str__(self):
        return self.Bill_id
class Order_Bill(models.Model):
    Order_Bill_id = models.AutoField(primary_key=True)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Bill_OP = models.ForeignKey(Bill_OP,on_delete=models.CASCADE)
    Qty = models.IntegerField()
    Total_price = models.IntegerField()
    Order_Date =  models.DateTimeField()
    def __str__(self):
        return self.Order_Bill_id
class Production_Bill(models.Model):
    Production_Bill_ID = models.AutoField(primary_key=True)
    Bill_OP = models.ForeignKey(Bill_OP,on_delete=models.CASCADE)
    Custormer = models.ForeignKey(Custormer,on_delete=models.CASCADE)
    Car_driver = models.CharField(max_length=255)
    H_Qty = models.IntegerField(null=True)
    T_Qty = models.IntegerField(null=True)
    M_Qty = models.IntegerField(null=True)
    L_Qty = models.IntegerField(null=True)
    H_Price = models.IntegerField(null=True)
    T_Price = models.IntegerField(null=True)
    M_Price = models.IntegerField(null=True)
    L_Price = models.IntegerField(null=True)
    H_Price_c = models.IntegerField(null=True)
    T_Price_c = models.IntegerField(null=True)
    M_Price_c = models.IntegerField(null=True)
    L_Price_c = models.IntegerField(null=True)
    Pay_status = models.BooleanField(null=True)
    Production_Date =  models.DateTimeField()
    def __str__(self):
        return self.Production_Bill_ID
class Exchange(models.Model):
    Exchange_id =models.AutoField(primary_key=True)
    Bill_OP = models.ForeignKey(Bill_OP,on_delete=models.CASCADE)
    price = models.IntegerField(null=True)
    iscomplete = models.BooleanField(null=True)