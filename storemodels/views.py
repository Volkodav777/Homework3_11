from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Product
from django_filters.views import FilterView
from storemodels import filters

# Create your views here.
class ProductListView(FilterView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    filterset_class = filters.Product_filter



class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class  ProductCreateView(CreateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'description', 'price', 'stock', 'category','type']
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'description', 'price', 'stock', 'category', 'image', 'type']
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
