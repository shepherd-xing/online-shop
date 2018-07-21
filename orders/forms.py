from django import forms
from .models import Order
#
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['province', 'city', 'address', 'name', 'tel', 'email']