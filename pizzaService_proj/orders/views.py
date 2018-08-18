from django.http import HttpResponse
from django.shortcuts import render


def search_form(request):
    return render(request, 'orders/search_form.html')


def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)