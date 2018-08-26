from django.test import TestCase, RequestFactory

from orders.views import *
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from orders.models import Customer
from orders.models import Pizza
from orders.models import Order

# def test_create_order(self):
#     request = RequestFactory().post('templates/orders/place_order.html')
#     response = add_order(request)
#     self.assertEqual(response.status_code, 200)



class ModelTestCase(TestCase):

    def setUp(self):
        self.customer_name = 'Test Name'
        self.customer_address = 'Test Address'
        self.customer = Customer(customer_name=self.customer_name, customer_address=self.customer_address)

        self.pizza_size = True
        self.pizza_flavor = 'Surprise'
        self.pizza = Pizza(pizza_size=self.pizza_size, pizza_flavor=self.pizza_flavor)

        self.order = Order(customer=self.customer, pizza=self.pizza)

    def test_model_create_customer(self):
        old_count = Customer.objects.count()
        self.customer.save()
        new_count = Customer.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.order_data = {'order_id': 14}
        self.response = self.client.post(reverse('create'), self.order_data, format='json')

    def test_create_order(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_order(self):
        order = Order.objects.last()
        print(Order.objects.count())
        response = self.client.get(
            reverse('details', order.order_id, format="json"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, order)

    def test_update_order(self):
        order = Order.objects.last()
        pizza = Pizza(pizza_size=True, pizza_flavor='New flavor')
        change_order = {'pizza': pizza}
        res = self.client.put(
            reverse('details', order.order_id, change_order, format='json'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_order(self):
        order = Order.objects.last()
        response = self.client.delete(
            reverse('details', order.order_id, format='json', follow=True))

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)