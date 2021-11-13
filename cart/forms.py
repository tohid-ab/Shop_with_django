from django import forms

PRODUCT_QUANTITY_CHOICE = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICE, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)