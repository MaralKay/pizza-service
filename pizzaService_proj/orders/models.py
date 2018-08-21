from django.db import models
from django.db.models import ForeignKey
import datetime


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=80)
    customer_address = models.CharField(max_length=100)

    def __str__(self):
        return u'%s %s' % (self.customer_id, self.customer_address)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)


class Pizza(models.Model):
    pizza_id = models.AutoField(primary_key=True)
    #   We assume that True value stands form 30cm and False value stands for 50cm
    pizza_size = models.BooleanField(default=True)
    pizza_flavor = models.CharField(default='Surprise', max_length=100)

    def __str__(self):
        if self.pizza_size:
            size = '30cm'
        else:
            size = '50cm'
        return u'%s %s' % (self.pizza_id, size)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    pizza = models.ForeignKey(Pizza)
    customer = models.ForeignKey(Customer)
    order_datetime = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return u'%s %s %s' % (self.order_id, self.customer.customer_name, self.pizza)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)