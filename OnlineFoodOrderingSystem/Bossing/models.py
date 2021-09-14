from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    is_admin = models.BooleanField()

    class meta:
        db_table = 'tblUser'

class Product(models.Model):
    product_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=20)
    product_category = models.CharField(max_length=10)
    price = models.FloatField()

    class meta:
        db_table = 'tblProduct'


