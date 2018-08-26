from datetime import datetime

from django.shortcuts import render

from orders.models import Order
from orders.models import Customer
from orders.models import Pizza

from orders.forms import OrdersForm
from orders.forms import EditForm
from rest_framework import generics

from orders.serializers import OrderSerializer, CustomerSerializer, PizzaSerializer


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            orders = Order.objects.filter(order_id__icontains=q)
            return render(request, 'orders/search_results.html', {'orders': orders, 'query': q})
    return render(request, 'orders/search_form.html', {'error': error})


def add_order(request):
    if request.POST.get('name') and request.POST.get('address') and request.POST.get('size')\
            and request.POST.get('flavor'):
        #   create customer
        customer_name = request.POST.get('name')
        customer_address = request.POST.get('address')
        customer = Customer(customer_name=customer_name, customer_address=customer_address)
        customer.save()
        #   create pizza
        pizza_size = request.POST.get('size')
        pizza_flavor = request.POST.get('flavor')
        pizza = Pizza(pizza_size=pizza_size, pizza_flavor=pizza_flavor)
        pizza.save()
        #   create order
        c = Customer.objects.latest('customer_id')
        p = Pizza.objects.latest('pizza_id')
        order = Order(pizza=p, customer=c)
        order.save()
        return render(request, 'orders/order_completed.html')
    return render(request, 'orders/place_order.html')


def show_orders_form(request):
    model = Order
    orders = Order.objects.all()
    if request.method == 'POST' and request.POST.get('action') == 'edit':
        return show_edit_form(request)
    elif request.method == 'POST' and request.POST.get('action') == 'delete':
        return remove_order(request)
    else:
        form = OrdersForm()
        return render(request, 'orders/orders.html', {'form': form, 'orders': orders})


def remove_order(request):
    if request.method == 'POST':
        form = OrdersForm()
        orders = Order.objects.all()
        order_id = request.POST.get('order-id')
        order = Order.objects.get(order_id=order_id)
        pizza = order.pizza
        customer = order.customer
        order.delete()
        pizza.delete()
        customer.delete()
        return render(request, 'orders/remove_orders.html', {'form': form, 'orders': orders})


def show_edit_form(request):
    model = Order
    if request.method == 'POST':
        form = EditForm(data=request.POST)
        order_id = request.POST.get('order-id')
        order = Order.objects.get(order_id=order_id)
        if form.is_valid():
            form.save()
        return render(request, 'orders/edit_order.html', {'form': form, 'order': order})
    else:
        form = OrdersForm()
        return render(request, 'orders/orders.html', {'form': form, 'orders': orders})


def edit_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order-id')
        order = Order.objects.get(order_id=order_id)
        #   get and update the customer
        customer = Customer.objects.get(customer_id=order.customer.customer_id)
        customer.customer_name = request.POST.get('name')
        customer.customer_address = request.POST.get('address')
        customer.save()
        #   get and update the pizza
        pizza = Pizza.objects.get(pizza_id=order.pizza.pizza_id)
        pizza.pizza_size = request.POST.get('size')
        pizza.pizza_flavor = request.POST.get('flavor')
        pizza.save()
        #   update order
        order.order_datetime = datetime.now()
        print(datetime.now)
        order.save()
        return render(request, 'orders/edited.html')


class CreateOrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()


class CreatePizzaView(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def perform_create(self, serializer):
        serializer.save()


class CreateCustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer