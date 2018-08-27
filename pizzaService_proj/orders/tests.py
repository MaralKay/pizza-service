from django.test import TestCase

from orders.views import *
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from orders.models import Customer
from orders.models import Pizza
from orders.models import Order


class ModelTestCase(TestCase):

    def setUp(self):
        self.customer_name = 'Test Name'
        self.customer_address = 'Test Address'
        self.customer = Customer(customer_name=self.customer_name, customer_address=self.customer_address)

        self.pizza_size = True
        self.pizza_flavor = 'Surprise'
        self.pizza = Pizza(pizza_size=self.pizza_size, pizza_flavor=self.pizza_flavor)

        self.order = Order(customer=self.customer, pizza=self.pizza)

    def test_model_create_order(self):
        old_count = Customer.objects.count()
        self.customer.save()
        new_count = Customer.objects.count()
        self.assertNotEqual(old_count, new_count)

        old_count = Pizza.objects.count()
        self.pizza.save()
        new_count = Pizza.objects.count()
        self.assertNotEqual(old_count, new_count)

        old_count = Order.objects.count()
        self.order = Order(customer=Customer.objects.latest('customer_id'), pizza=Pizza.objects.latest('pizza_id'))
        self.order.save()
        new_count = Order.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.customer_name = 'Test Name'
        self.customer_address = 'Test Address'
        self.customer_data = {'customer_name': 'Test Name', 'customer_address': 'Test Address'}
        self.customer = Customer.objects.create(customer_name=self.customer_name, customer_address=self.customer_address)

        self.pizza_size = True
        self.pizza_flavor = 'Surprise'
        self.pizza_data = {'pizza_size': True, 'pizza_flavor': 'Surprise'}
        self.pizza = Pizza.objects.create(pizza_size=self.pizza_size, pizza_flavor=self.pizza_flavor)

        self.order = Order(customer=self.customer, pizza=self.pizza)
        self.order_data = {'customer': self.customer, 'pizza': self.pizza}
        self.order = Order.objects.create(customer=self.customer, pizza=self.pizza)

    def test_get_order(self):
        order = self.order
        response = self.client.get(reverse('details_id', kwargs={'pk': order.order_id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_order(self):
        order = self.order
        response = self.client.delete(reverse('details_id', kwargs={'pk': order.order_id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
