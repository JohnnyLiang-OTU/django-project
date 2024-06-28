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