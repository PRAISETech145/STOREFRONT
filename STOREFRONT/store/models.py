from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)

class Customer(models.Model):
    MEMBERSHIP=[
        ('S','Silver'),
        ('B','Bronze'),
        ('G','Gold'),
    ]
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.EmailField(unique=True)
    phone=models.CharField()
    birthdate=models.DateField(blank=True) 
    membership=models.CharField(max_length=1,choices=MEMBERSHIP,default="S")  

class Order(models.Model):
    PAYMENT_STATUS=[
        ('P','pending'),
        ('C','completed'),
        ('F','failed'),
    ]
    place_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STATUS,default='P')

