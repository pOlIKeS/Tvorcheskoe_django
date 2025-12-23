from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Product

class ProductModelTest(TestCase):
    def setUp(self):
        # Create a category
        self.category = Category.objects.create(
            name="Овощи",
            slug="vegetables"
        )
        
        # Create a product
        self.product = Product.objects.create(
            category=self.category,
            name="Свежая морковь",
            slug="fresh-carrot",
            description="Сочная и сладкая морковь",
            price=150.00,
            weight="1 кг",
            calories="35 ккал",
            protein="1.3г",
            fat="0.1г",
            carbs="7.2г",
            in_stock=True
        )

    def test_product_creation(self):
        """Test that a product can be created"""
        self.assertEqual(self.product.name, "Свежая морковь")
        self.assertEqual(self.product.category, self.category)
        self.assertTrue(self.product.in_stock)

    def test_product_formatted_price(self):
        """Test that formatted_price method works correctly"""
        self.assertEqual(self.product.formatted_price(), "150.00 ₽")

    def test_product_get_absolute_url(self):
        """Test that get_absolute_url method works correctly"""
        expected_url = f"/{self.product.slug}/"
        self.assertEqual(self.product.get_absolute_url(), expected_url)