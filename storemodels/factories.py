import factory
from factory.django import ImageField


from storemodels.models import Category, Product, Customer, Order, OrderItem


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    description = factory.Faker('text')
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    stock = factory.Faker('random_int', min=1, max=100)
    category = factory.SubFactory(CategoryFactory)
    type = 'sneakers'

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    email = factory.Faker('email')

class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    customer = factory.SubFactory(CustomerFactory)
    complete = False

class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem

    product = factory.SubFactory(ProductFactory)
    order = factory.SubFactory(OrderFactory)
    quantity = factory.Faker('random_int', min=1, max=10)
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)