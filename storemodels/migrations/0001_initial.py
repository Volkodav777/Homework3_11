# Generated by Django 5.1.2 on 2024-10-09 13:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата заказа')),
                ('complete', models.BooleanField(default=False, verbose_name='Заказ завершен')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='storemodels.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-date_ordered'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('description', models.TextField(blank=True, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('stock', models.PositiveIntegerField(verbose_name='Количество на складе')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Изображение товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='storemodels.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за единицу')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='storemodels.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='storemodels.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Позиция заказа',
                'verbose_name_plural': 'Позиции заказа',
            },
        ),
    ]
