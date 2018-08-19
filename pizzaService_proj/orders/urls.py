from django.conf.urls import url
import orders.views as views


urlpatterns = [
    url(r'^search/$', views.search),
    url(r'^orders/$', views.get_orders),
    url(r'^place-order/$', views.add_order),
]