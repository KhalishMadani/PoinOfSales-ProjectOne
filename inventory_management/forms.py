from django import forms
from .models import CategoryProduct, Product, Distributor, ProductList

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryProduct
        exclude = ['created_at',]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at']

class DistributorForm(forms.ModelForm):
    class Meta:
        model = Distributor
        exclude = ['created_at',]

class ProductListForm(forms.ModelForm):
    class Meta:
        model = ProductList
        exclude = ['created_at',]