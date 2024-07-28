from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

from .models import CategoryProduct, Vendor, RegisterProduct
from .forms import CategoryForm, VendorForm, RegisterProductForm, ProductForm, ProductFormRenteng


# Create your views here.
class CategoryInput(View):
    template = 'register_category.html'

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
            return HttpResponseRedirect(reverse_lazy('register_category'))
        else:
            print(f'category form error: {form}')
            messages.error(request, 'Kategori Gagal Ditambahkan')
            return HttpResponseRedirect(reverse_lazy('register_category'))
        

class VendorInput(View):
    template = 'register_vendor.html'

    def get(self, request):
        context = {
            'title': 'Input Distributor'
        }
        return render(request, self.template, context)
    
    def post(self, request):
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Distributor Berhasil Ditambahkan')
            return HttpResponseRedirect(reverse_lazy('register_vendor'))
        else:
            print(f'category form error: {form}')
            messages.error(request, 'Distirbutor Gagal Ditambahkan')
            return HttpResponseRedirect(reverse_lazy('register_vendor'))
        

class RegisterProductInput(View):
    template = 'register_product.html'

    def get(self, request):
        context = {
            'title': 'Input Product List'
        }
        return render(request, self.template, context)
    
    def post(self, request):
        form = RegisterProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk Baru Berhasil Ditambahkan')
            return HttpResponseRedirect(reverse_lazy('register_product'))
        else:
            print(f'category form error: {form}')
            messages.error(request, 'Produk Baru Gagal Ditambahkan')
            return HttpResponseRedirect(reverse_lazy('register_product'))
        

class ProductInput(View):
    template = 'input_product.html'

    def get(self, request):
        category_list = CategoryProduct.objects.all()
        vendor_list = Vendor.objects.all()
        context = {
            'category_list': category_list,
            'vendor_list': vendor_list
        }
        return render(request, self.template, context)
    
    def post(self, request):
        form_data = request.POST.copy()
        form_data['current_pieces'] = form_data.get('pieces')
        # form_renteng = ProductFormRenteng(form_data)
        form = ProductForm(form_data)

        # if form_renteng.is_valid():
        #     product = form_renteng.save()
        #     context = {'product': product}
        #     messages.success(request, 'Produk Berhasil Disimpan')
        #     return render(request, 'partial/just_created_item.html', context)
        
        if form.is_valid():
            product = form.save()
            context = {'product': product}
            messages.success(request, 'Produk Berhasil Disimpan')
            return render(request, 'partial/just_created_item.html', context)
        
        else:
            # for renteng in form_renteng.errors:
            #     print(renteng)

            for error in form.errors:
                print(error)
            messages.error(request, 'Produk Gagal Disimpan')
            return HttpResponseRedirect(reverse_lazy('create_product'))
    

def barcode_scanner(request):
    if request.method == 'GET':
        get_value = request.GET.get('value')
        print(f'value received: {get_value}')

        find_value = get_object_or_404(RegisterProduct, product_barcode=get_value)

        try:
            data = {
                'name': find_value.product_name,
            }

            return JsonResponse(data)
        
        except:
            print(f'value error not found')