from django.db import models
from tkinter import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    CategoryName=models.CharField(max_length=50)

    def __str__(self):
        return self.CategoryName

class Product(models.Model):
    productName=models.CharField(max_length=50)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    price=models.IntegerField()
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.productName

class Customer(models.Model):
    name=models.CharField(max_length=50)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    email =models.CharField(max_length=100)

    def __str__(self):
        return self.name
class OrderItems(models.Model):
    name=models.ForeignKey('Customer',on_delete=models.CASCADE)
    product=models.ForeignKey('Product',on_delete=models.CASCADE)
    quantity=models.IntegerField()
    def __str__(self):
        return self.name
