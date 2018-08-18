from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=80)
    customer_address = models.CharField(max_length=100)


class Pizza(models.Model):
    pizza_id = models.AutoField(primary_key=True)
    #   We assume that True value stands form 30cm and False value stands for 50cm
    pizza_size = models.BooleanField(default=True)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    pizza = models.ForeignKey(Pizza)
    customer = models.ForeignKey(Customer)