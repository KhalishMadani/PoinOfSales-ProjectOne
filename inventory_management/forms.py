from django import forms
from .models import CategoryProduct, Product, Vendor, RegisterProduct

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryProduct
        exclude = ['created_at',]
        widgets = {
            'category_name': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Kategori Baru'
            }),
        }

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        exclude = ['created_at',]
        widgets = {
            'vendor_name': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'distributor'
            }),
        }

class RegisterProductForm(forms.ModelForm):
    class Meta:
        model = RegisterProduct
        exclude = ['created_at',]

class ProductFormRenteng(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['renteng', 'created_at']