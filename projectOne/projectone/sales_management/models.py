from django.db import models

from inventory_management.models import InventoryManagement

# Create your models here.
class Sales_Management(models.Model):
    class Meta:
        db_table = 'transaction'

    transaction_id = models.CharField(primary_key=True, max_length=50)
    product_id = models.ForeignKey(InventoryManagement, on_delete=models.PROTECT, db_column='product_id')
    user_id = models.CharField(max_length=50)
    unit_sold_price = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)