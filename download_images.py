#!/usr/bin/env python
import os
import sys
import json
import requests
from urllib.parse import urlparse
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecoshop.settings')
django.setup()

from products.models import Product
from django.core.files.base import ContentFile

def download_image(url, product_name):
    """Download image from URL and return filename"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # If no filename, create one based on product name
        if not filename or '.' not in filename:
            filename = f"{product_name.replace(' ', '_').lower()}.jpg"
        
        return ContentFile(response.content), filename
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None, None

def download_product_images():
    # Read products from JSON file
    with open('products.json', 'r', encoding='utf-8') as f:
        products_data = json.load(f)
    
    print(f"Processing {len(products_data)} products...")
    
    for product_data in products_data:
        try:
            # Find product in database
            product = Product.objects.get(name=product_data['name'])
            
            # Get first image URL
            if product_data.get('image_urls') and len(product_data['image_urls']) > 0:
                image_url = product_data['image_urls'][0]
                print(f"Downloading image for {product.name} from {image_url}")
                
                # Download image
                image_content, filename = download_image(image_url, product.name)
                if image_content and filename:
                    # Save image to product
                    product.image.save(filename, image_content, save=True)
                    print(f"  Saved image: {filename}")
                else:
                    print(f"  Failed to download image")
            else:
                print(f"No images for {product.name}")
                
        except Product.DoesNotExist:
            print(f"Product not found: {product_data['name']}")
        except Exception as e:
            print(f"Error processing {product_data['name']}: {e}")
    
    print("Image download complete!")

if __name__ == "__main__":
    download_product_images()