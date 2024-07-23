from django.urls import path
from .views import ProductListView
from . import views

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/add/', views.add_product, name='add_product'),
    path('')
    
]