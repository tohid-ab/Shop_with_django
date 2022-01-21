from django.db import models
from django.urls import reverse
# Create your models here.
from django.utils.html import format_html


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    class Meta:
        ordering = ('-name',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ManyToManyField(Category, related_name='products', verbose_name='دسته بندی')
    name = models.CharField(max_length=200, db_index=True, verbose_name='نام')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='آدرس')
    image = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True, verbose_name='عکس')
    description = models.TextField(blank=True, verbose_name='متن')
    price = models.IntegerField(verbose_name='قیمت')
    available = models.BooleanField(default=True, verbose_name='موجوده')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name

    def image_tag(self):
        return format_html("<img width=50 style='border-radius:5px;' src='{}'>".format(self.image.url))
    image_tag.short_description = 'عکس'
