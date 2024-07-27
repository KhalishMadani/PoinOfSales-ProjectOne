from django import forms
from .models import CategoryProduct, Product, Vendor, RegisterProduct

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryProduct
        exclude = ['created_at',]

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        exclude = ['created_at',]

class RegisterProductForm(forms.ModelForm):
    class Meta:
        model = RegisterProduct
        exclude = ['created_at',]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at']