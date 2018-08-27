from rest_framework import serializers
from .models import Order, Customer, Pizza

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('order_id', 'customer', 'pizza', 'order_datetime')
        read_only_fields = ('order_id', 'order_datetime')


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('customer_id', 'customer_name', 'customer_address')
        read_only_field = 'customer_id'


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = ('pizza_id', 'pizza_size', 'pizza_flavor')
        read_only_field = 'pizza_id'