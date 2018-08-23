from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Order
        fields = ('order_id', 'customer', 'pizza', 'order_datetime')
        read_only_fields = ('order_id', 'order_datetime')