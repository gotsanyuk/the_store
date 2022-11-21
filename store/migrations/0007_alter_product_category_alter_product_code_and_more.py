# Generated by Django 4.1.2 on 2022-10-13 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='store.category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=255, verbose_name='id код продукту'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='product',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Ціна'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Наявність'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Кількість'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата редагування'),
        ),
    ]
