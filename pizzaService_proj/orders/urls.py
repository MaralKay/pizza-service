from django.conf.urls import url
import orders.views as views


urlpatterns = [
    url(r'^search/$', views.search),
    url(r'^place-order/$', views.add_order),
    url(r'^orders/$', views.show_orders_form),
    url(r'^remove-orders/$', views.remove_order),
    url(r'^edit-order/$', views.show_edit_form),
    url(r'^edited/$', views.edit_order),
]