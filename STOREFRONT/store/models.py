from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collections=models.ForeignKey('Collections',on_delete=models.PROTECT)
    promotions=models.ManyToManyField('Promotion')
    slug=models.SlugField(null=True)

class Customer(models.Model):
    MEMBERSHIP=[
        ('S','Silver'),
        ('B','Bronze'),
        ('G','Gold'),
    ]
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=9)
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
    item=models.ForeignKey('OrderItem',on_delete=models.CASCADE,related_name="+")
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)

class Address(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    street=models.CharField(max_length=250)
    city=models.CharField(max_length=200)

class Collections(models.Model):
    title=models.CharField(max_length=100)
    feature_product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name="+")

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)
class Cart(models.Model):
      created_at=models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)   
    quantity=models.PositiveSmallIntegerField()

class Promotion(models.Model):
    description=models.CharField(max_length=300)
    discount=models.FloatField()    
      

