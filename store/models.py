from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True,
                                     blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('store:category_filter', args={self.slug})


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products', verbose_name='Категорія')
    name = models.CharField(max_length=255, verbose_name='Назва')
    slug = models.SlugField(max_length=200)
    code = models.CharField(max_length=255, verbose_name='id код продукту')
    price = models.IntegerField(verbose_name='Ціна')
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='Кількість')
    image_url = models.URLField(blank=True, null=True, verbose_name='Зображення')
    note = models.TextField(blank=True, null=True, verbose_name='Опис')
    status = models.BooleanField(default=True, verbose_name='Наявність')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата редагування')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('store:product_detail', args={self.slug, })
