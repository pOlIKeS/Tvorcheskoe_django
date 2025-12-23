from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Category, Product
from .models import Order, OrderItem

class OrderModelTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
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
        
        # Create an order
        self.order = Order.objects.create(
            user=self.user,
            phone="+71234567890",
            address="Тестовый адрес, 123",
            status="new"
        )
        
        # Create an order item
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            price_at_order=150.00
        )

    def test_order_creation(self):
        """Test that an order can be created"""
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.phone, "+71234567890")
        self.assertEqual(self.order.status, "new")

    def test_order_item_creation(self):
        """Test that an order item can be created"""
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.product, self.product)
        self.assertEqual(self.order_item.quantity, 2)
        self.assertEqual(self.order_item.price_at_order, 150.00)

    def test_order_total_price(self):
        """Test that order total price calculation works correctly"""
        expected_total = 150.00 * 2  # 2 items at 150.00 each
        self.assertEqual(self.order.total_price(), expected_total)

    def test_order_item_total_price(self):
        """Test that order item total price calculation works correctly"""
        expected_total = 150.00 * 2  # 2 items at 150.00 each
        self.assertEqual(self.order_item.total_price(), expected_total)