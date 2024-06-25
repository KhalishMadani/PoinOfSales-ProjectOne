from django.shortcuts import render
from django.views.generic import ListView

from .models import InventoryManagement


# Create your views here.
class ListInventory(ListView):
    model =InventoryManagement
    template_name = 'listview.html'
    context_object_name = 'items'