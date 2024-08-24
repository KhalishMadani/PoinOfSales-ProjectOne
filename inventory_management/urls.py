from django.urls import path

from .import views

urlpatterns = [
     path('category-input-form/',
          views.CategoryPage.as_view(),
          name='register_category'
          ),
     
     path('distirbutor-input-form/',
          views.VendorInput.as_view(),
          name='register_vendor'
          ),

     path('product-new-input-form/',
          views.RegisterProductInput.as_view(),
          name='register_product'
          ),
     
     path('product-input-form/',
          views.ProductInput.as_view(),
          name='create_product'
          ),


     # fetch function    
     path('fetch-product-function/',
          views.barcode_scanner,
          name='scanner'
          ),

     path('create-category-htmx/',
          views.create_category,
          name='create_category'
          ),

     path('create-vendor-htmx/',
          views.create_vendor,
          name='create_vendor'
          )
]
