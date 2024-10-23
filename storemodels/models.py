from django.db import models
from django.utils import timezone
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    NAME_CHOICES = [('sneakers', 'Кроссовки'),('Rubber boots', 'Резиновые сапоги'),('deck shoes', 'Топсайдеры'),
                    ('Hat', 'Шляпы'), ('Accessories', 'Аксессуары'), ('trinket', 'Безделушки'), ('lingerie', 'нижнее белье'),
                    ('shoes', 'Обувь')]

    name = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Количество на складе')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products',verbose_name='Категория')
    image = models.ImageField( upload_to='products/',blank=True,null=True,verbose_name='Изображение товара')

    type = models.CharField(max_length=50,choices=NAME_CHOICES,default='Кроссовки',verbose_name='Тип товара',blank=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def __str__(self):
        return self.name


    def display_price(self):
        return f"{self.price} ₽"



class Customer(models.Model):
    name = models.CharField(max_length=50,verbose_name='Имя')
    surname = models.CharField(max_length=50,verbose_name='Фамилия')
    email = models.EmailField(unique=True,verbose_name='Электронная почта')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['surname']

    def __str__(self):
        return f"{self.name} {self.surname}"


    def full_name(self):
        return f"{self.name} {self.surname}"



class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='orders',verbose_name='Клиент')
    date_ordered = models.DateTimeField(default=timezone.now,verbose_name='Дата заказа')
    complete = models.BooleanField(default=False,verbose_name='Заказ завершен')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date_ordered']

    def __str__(self):
        return f"Заказ №{self.id} от {self.date_ordered}"


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_items',verbose_name='Товар')
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items',verbose_name='Заказ')
    quantity = models.PositiveIntegerField(default=1,verbose_name='Количество')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Цена за единицу')

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_total(self):
        return self.quantity * self.price
