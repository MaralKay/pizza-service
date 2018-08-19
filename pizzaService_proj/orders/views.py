from django.http import HttpResponse
from django.shortcuts import render

from orders.models import Order


def search_form(request):
    return render(request, 'orders/search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        orders = Order.objects.filter(order_id__icontains=q)
        return render(request, 'orders/search_results.html',
                      {'orders': orders, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def getOrders(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders.html',
                      {'orders': orders})