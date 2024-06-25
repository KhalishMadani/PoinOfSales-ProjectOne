from django.db import models

# Create your models here.
class InventoryManagement(models.Model):
    class Meta:
        db_table = 'inventory_management'

    product_id = models.CharField(primary_key=True, max_length=50)
    product_name = models.CharField(max_length=50)
    unit_price = models.IntegerField()
    bought_quantity = models.IntegerField()
    in_stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)