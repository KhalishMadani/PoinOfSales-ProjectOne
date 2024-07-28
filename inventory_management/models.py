from django.db import models

class CategoryProduct(models.Model):
    category_name = models.CharField(max_length=50, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

class RegisterProduct(models.Model):
    product_barcode = models.CharField(max_length=50, primary_key=True)
    product_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    # product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_type = models.CharField(max_length=50)
    packing_qty = models.IntegerField()
    renteng = models.IntegerField(null=True)
    pieces = models.IntegerField()
    current_pieces = models.IntegerField()
    purchase_date = models.DateTimeField()
    expired_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    product_barcode = models.ForeignKey(RegisterProduct, db_column='product_barcode', on_delete=models.PROTECT)
    category_name = models.ForeignKey(CategoryProduct, db_column='category_name', on_delete=models.PROTECT)
    vendor_name = models.ForeignKey(Vendor, db_column='vendor_name', on_delete=models.PROTECT)