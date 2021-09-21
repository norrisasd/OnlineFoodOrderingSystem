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

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateField(auto_now_add=True)
    total_price = models.FloatField()

    class meta:
        db_table = 'order'

class Order_Details(models.Model):
    order_details_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class meta:
        db_table = 'order_details'

class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    delivery_carrier = models.CharField(max_length=50)

    class meta:
        db_table = 'delivery'

class Receiver(models.Model):
    receiver_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery_id = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    receiver_name = models.CharField(max_length=100)
    receiver_contact = models.CharField(max_length=11)
    receiver_address = models.CharField(max_length=100)
    date_received = models.DateField()
    time_received = models.TimeField()
    class meta:
        db_table = 'receiver'
