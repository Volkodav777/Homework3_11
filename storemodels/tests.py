from http.client import responses

from django.test import TestCase
from django.urls import reverse

from storemodels import factories, models
from storemodels.factories import CategoryFactory, ProductFactory
from storemodels.models import Product


# Create your tests here.

class ProductViewTest(TestCase):

        def setUp(self):
            self.category = CategoryFactory()
            self.product = ProductFactory(category=self.category)

        def test_product_list_view(self):
            url = reverse('product_list')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(self.product, response.context['products'])

        def test_product_detail_view(self):
            url = reverse('product_detail', args=[self.product.id])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.context['product'], self.product)

        def test_product_create_view(self):
            url = reverse('product_create')
            data = {
                'name': 'New Product',
                'description': 'A new product',
                'price': '100.00',
                'stock': 50,
                'category': self.category.id,
                'type': 'sneakers'
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(Product.objects.count(), 2)  # Было 1, стало 2

        def test_product_update_view(self):
            url = reverse('product_update', args=[self.product.id])
            data = {
                'name': 'Updated Product',
                'description': 'Updated description',
                'price': '150.00',
                'stock': 30,
                'category': self.category.id,
                'type': 'sneakers'
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 302)
            self.product.refresh_from_db()
            self.assertEqual(self.product.name, 'Updated Product')

        def test_product_delete_view(self):
            url = reverse('product_delete', args=[self.product.id])
            response = self.client.post(url)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(Product.objects.count(), 0)