from django.urls import path
from .views import ProductListView, ProductDetailView, SupplierMapView, suppliers_json

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('suppliers/map/', SupplierMapView.as_view(), name='supplier_map'),
    path('suppliers/json/', suppliers_json, name='suppliers_json'),
]