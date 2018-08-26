from django.conf.urls import url
import orders.views as views

from orders.views import CreateOrderView, CreateCustomerView, CreatePizzaView

from orders.views import DetailsView

urlpatterns = [
    url(r'^search/$', views.search),
    url(r'^place-order/$', views.add_order),
    url(r'^orders/$', views.show_orders_form),
    url(r'^remove-orders/$', views.remove_order),
    url(r'^edit-order/$', views.show_edit_form),
    url(r'^edited/$', views.edit_order),
    #   api endpoints
    url(r'^add-order/$', CreateOrderView.as_view(), name='create'),
    url(r'^add-customer/$', CreateCustomerView.as_view(), name='create'),
    url(r'^add-pizza/$', CreatePizzaView.as_view(), name='create'),
    url(r'^order-details/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
]