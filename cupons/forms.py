from django import forms


class CouponApply(forms.Form):
    code = forms.CharField()