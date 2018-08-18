from django.conf.urls import url
import orders.views as views


urlpatterns = [
    url(r'search-form/$', views.search_form),
    url(r'^search/$', views.search),
]