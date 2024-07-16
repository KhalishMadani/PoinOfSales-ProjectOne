from django.db import models

class CategoryProduct(models.Model):
    category_id = models.CharField(primary_key=True, max_length=50)
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class ProductList(models.Model):
    product_name = models.CharField(primary_key=True, max_length=50)
    carton = models.IntegerField()
    barcode = models.CharField(max_length=50, null=True)
    qr_code = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Distributor(models.Model):
    company_name = models.CharField(max_length=50, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_barcode = models.CharField(max_length=50)
    pieces = models.IntegerField()
    current_pieces = models.IntegerField()
    purchase_date = models.DateTimeField()
    expired_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    product_name = models.ForeignKey(ProductList, db_column='product_name', on_delete=models.PROTECT, null=True)
    category_id = models.ForeignKey(CategoryProduct, db_column='category_id', on_delete=models.PROTECT, null=True)
    company_name = models.ForeignKey(Distributor, db_column='company_name', on_delete=models.PROTECT, null=True)