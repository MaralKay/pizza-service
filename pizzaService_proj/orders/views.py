from django.http import HttpResponse
from django.shortcuts import render

from orders.models import Order


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