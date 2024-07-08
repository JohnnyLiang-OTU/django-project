from django.test import TestCase
from .models import Product
from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile
import os
# Create your tests here.
class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            product_id="12345",
            description="Test Product",
            image=SimpleUploadedFile(name='static/images/aisin.png', content=b'', content_type='image/png')
        )

    def test_product_creation(self):
        self.assertEqual(self.product.product_id, "12345")
        self.assertEqual(self.product.description, "Test Product")
        self.assertTrue(self.product.image)

    def test_product_str_method(self):
        self.assertEqual(str(self.product), "12345Test Product")
    
    def test_image_deleted_on_product_deletion(self):
        image_path = self.product.image.path
        self.product.delete()
        print(image_path, os.path.exists(image_path))
        self.assertFalse(os.path.exists(image_path))

from django.test import TestCase, Client
from django.conf import settings

class Error500Test(TestCase):
    def setUp(self):
        self.client = Client()
        self.original_debug = settings.DEBUG
        settings.DEBUG = False

    def tearDown(self):
        settings.DEBUG = self.original_debug

    def test_500_view(self):
        response = self.client.get('/test-500/')
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, '500.html')