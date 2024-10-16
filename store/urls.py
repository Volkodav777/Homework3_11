from django.contrib import admin
from django.urls import path
from storemodels.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]



