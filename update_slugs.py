#!/usr/bin/env python
import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecoshop.settings')
django.setup()

from products.models import Product

def update_product_slugs():
    products = Product.objects.all()
    print(f"Updating slugs for {products.count()} products...")
    
    for product in products:
        # Clear the slug to trigger regeneration
        old_slug = product.slug
        product.slug = ''
        product.save()
        print(f"Updated: {product.name}")
        print(f"  Old slug: {old_slug}")
        print(f"  New slug: {product.slug}")
        print()
    
    print("All product slugs updated successfully!")

if __name__ == "__main__":
    update_product_slugs()