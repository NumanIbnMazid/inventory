from django.db import models
from django.conf import settings
from accounts.utils import unique_slug_generator, time_str_mix_slug, upload_product_image_path
from django.db.models.signals import post_save, pre_save
from django.template.defaultfilters import slugify

class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='title')
    slug = models.SlugField(unique=True, verbose_name='slug')
    image = models.ImageField(
        upload_to=upload_product_image_path, null=True, blank=True, verbose_name='image')
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity')
    price = models.FloatField(default=0.00, verbose_name='price')
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name='description')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")
        ordering = ["-updated_at"]


class Order(models.Model):
    SELL = 0
    PURCHASE = 1
    ORDER_TYPE_CHOICES = (
        (SELL, 'Sell'),
        (PURCHASE, 'Purchase')
    )
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer_order', verbose_name='customer')
    slug = models.SlugField(unique=True, verbose_name='slug')
    total = models.FloatField(verbose_name='total')
    order_date = models.DateTimeField(
        auto_now_add=True, verbose_name='order date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")
        ordering = ["-order_date"]

    def __str__(self):
        return self.customer.username


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_line', verbose_name='order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order_line', verbose_name='product')
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')

    class Meta:
        verbose_name = ("Order Line")
        verbose_name_plural = ("Order Lines")
        ordering = ["-created_at"]

    def __str__(self):
        return self.order.customer.username


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver, sender=Product)


def order_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        if len(instance.customer.username) > 10:
            username = instance.customer.username.lower()[:10]
        else:
            username = instance.customer.username.lower()
        slug_binding = slugify(username) + "_" + time_str_mix_slug()
        # print(slug_binding)
        instance.slug = slug_binding


pre_save.connect(order_slug_pre_save_receiver, sender=Order)
