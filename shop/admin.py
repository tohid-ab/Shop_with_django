from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class Productsadmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'image_tag', 'available', 'categorye', 'updated']
    list_filter = ['available', 'category', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    def categorye(self, obj):
        return "|".join([Category.name for Category in obj.category.all()])
    categorye.short_descriptions = 'دسته بندی'
