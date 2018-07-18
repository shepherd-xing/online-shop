from django import forms
from .models import CartModel

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    # False:累加；True:给定值
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CartForm(forms.ModelForm):
    class Meta:
        model = CartModel
        fields = ('quantity', 'update')