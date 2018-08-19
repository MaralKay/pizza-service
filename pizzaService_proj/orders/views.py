from django.http import HttpResponse
from django.shortcuts import render
from orders.models import Order
from orders.models import Customer
from orders.models import Pizza


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


def get_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders.html', {'orders': orders})


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


#def delete_order(request):
