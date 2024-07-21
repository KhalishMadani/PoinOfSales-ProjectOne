from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

from .models import CategoryProduct, Distributor, ProductList
from .forms import CategoryForm, DistributorForm, ProductListForm, ProductForm


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
            return HttpResponseRedirect(reverse_lazy('product_input_new'))
        else:
            print(f'category form error: {form}')
            messages.error(request, 'Produk Baru Gagal Ditambahkan')
            return HttpResponseRedirect(reverse_lazy('product_input_new'))
        
class ProductInput(View):
    template = 'input_product.html'

    def get(self, request):
        category_list = CategoryProduct.objects.all()
        vendor_list = Distributor.objects.all()
        context = {
            'category_list': category_list,
            'vendor_list': vendor_list
        }
        return render(request, self.template, context)
    
    def post(self, request):
        form_data = request.POST.copy()
        form_data['current_pieces'] = form_data.get('pieces')
        form = ProductForm(form_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk Berhasil Disimpan')
            return HttpResponseRedirect(reverse_lazy('product_input'))
        else:
            print(f'category form error: {form}')
            messages.error(request, 'Produk Gagal Disimpan')
            return HttpResponseRedirect(reverse_lazy('product_input'))
    


def barcode_scanner(request):
    if request.method == 'GET':
        get_value = request.GET.get('value')
        print(f'value received: {get_value}')

        find_value = get_object_or_404(ProductList, barcode=get_value)

        try:
            data = {
                'name': find_value.product_name,
            }

            return JsonResponse(data)
        
        except:
            print(f'value error not found')