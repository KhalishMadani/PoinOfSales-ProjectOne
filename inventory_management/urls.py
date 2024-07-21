from django.urls import path

from .import views

urlpatterns = [
    path('category-input-form/',
         views.CategoryInput.as_view(),
         name='category_input'
         ),
    
    path('distirbutor-input-form/',
         views.DistributorInput.as_view(),
         name='distributor_input'
         ),

    path('product-new-input-form/',
         views.ProductListInput.as_view(),
         name='product_input_new'
         ),
    
    path('product-input-form/',
         views.ProductInput.as_view(),
         name='product_input'
         ),


    # fetch function    
    path('fetch-product-function/',
         views.barcode_scanner,
         name='scanner'
         ),
]
