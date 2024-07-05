from django.urls import path

from .import views

urlpatterns = [
    path('inventory-manager/', views.ListInventory.as_view(), name="inventory_list"),
]
