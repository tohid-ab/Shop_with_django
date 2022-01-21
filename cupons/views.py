from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupons
from .forms import CouponApply
from django.contrib import messages
# Create your views here.


@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApply(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupons.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True)
            request.session['coupon_id'] = coupon.id
            messages.success(request, 'کد شما اعمال شد')

        except:
            request.session['coupon_id'] = None
            messages.error(request, 'خطا')

    return redirect('cart:cart_detail')