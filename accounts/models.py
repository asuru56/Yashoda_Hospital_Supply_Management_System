from django.db import models

#Create you models here

class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    amount = models.FloatField(null=True)
    code = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200,null=True)
    unit = models.FloatField(null=True)
    department = models.CharField(max_length=200,null=True)
    balance = models.FloatField(null=True)
    kit =models.CharField(max_length=200,null=True)
    data_created = models.DateTimeField(auto_now=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
            return self.name

class Order(models.Model):
    STATUS = (
            ('Pending','Pending'),
            ('Out for Delivery', 'Out for Delivery'),
            ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    products = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    data_created = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    tags = models.ManyToManyField(Tag)



    def __str__(self):
            return self.status
