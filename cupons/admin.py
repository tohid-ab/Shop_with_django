from django.contrib import admin
from .models import Coupons
# Register your models here.


@admin.register(Coupons)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discout', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']