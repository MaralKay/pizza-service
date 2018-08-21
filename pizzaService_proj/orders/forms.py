from django.forms import ModelForm

from orders.models import Order


class OrdersForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class EditForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
