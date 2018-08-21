from django.test import TestCase, RequestFactory

from orders.views import *


class OrderTests(TestCase):

    def test_create_order(self):
        request = RequestFactory().post('templates/orders/place_order.html')
        response = add_order(request)
        self.assertEqual(response.status_code, 200)

