from django.db import models

# Create your models here.

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    is_admin = models.BooleanField()

    class meta:
        db_table = 'user'

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    price = models.FloatField()

    class meta:
        db_table = 'product'


