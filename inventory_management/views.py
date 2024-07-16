from django.shortcuts import render
from django.views.generic import ListView, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import CategoryProduct
from .forms import CategoryForm, DistributorForm, ProductListForm


# Create your views here.
class CategoryInput(View):
    template = 'input_category.html'

    def get(self,request):
        context = {
            'title': 'Input Kategori'
        }
        return render(request, self.template, context)
    
    def post(self,request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori Berhasil Ditambahkan')
            return HttpResponseRedirect(reverse_lazy('category_input'))
        else:
            print(f'category form error: {form}')
            messages.error(request, 'Kategori Gagal Ditambahkan')
            return HttpResponseRedirect(reverse_lazy('category_input'))
        
class DistributorInput(View):
    template = 'input_distributor.html'

    def get(self, request):
        context = {
            'title': 'Input Distributor'
        }
        return render(request, self.template, context)
    
    def post(self, request):
        form = DistributorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Distributor Berhasil Ditambahkan')
            return HttpResponseRedirect(reverse_lazy('distributor_input'))
        else:
            print(f'category form error: {form}')
            messages.error(request, 'Distirbutor Gagal Ditambahkan')
            return HttpResponseRedirect(reverse_lazy('distributor_input'))
        

class ProductListInput(View):
    template = 'input_product_new.html'

    def get(self, request):
        context = {
            'title': 'Input Product List'
        }
        return render(request, self.template, context)
    
    def post(self, request):
        form = ProductListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk Baru Berhasil Ditambahkan')
            return HttpResponseRedirect(reverse_lazy('product_input'))
        else:
            print(f'category form error: {form}')
            messages.error(request, 'Produk Baru Gagal Ditambahkan')
            return HttpResponseRedirect(reverse_lazy('product_input'))