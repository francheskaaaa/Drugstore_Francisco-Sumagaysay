from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    username = models.CharField(max_length=500, unique=True, error_messages={"unique": "Username already exists."})
    email = models.EmailField(unique=True, error_messages={"unique": "Email already exists."})
    password = models.CharField(max_length=128)
    role = models.BooleanField(default=False)

class AuditLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    action = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    report_type = models.CharField(max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=500)

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    address = models.TextField()

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=500)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.PROTECT)

class PurchaseOrder(models.Model):
    purchase_order_id = models.AutoField(primary_key=True)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    arrival_date = models.DateTimeField(null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class PurchaseOrderDetails(models.Model):
    purchase_order_detail_id = models.AutoField(primary_key=True)
    purchase_order_id = models.ForeignKey(PurchaseOrder, on_delete=models.PROTECT)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)  # Foreign key to Product
    batch_number = models.CharField(  # New field for batch tracking
        max_length=100,
        null=True,
        blank=True,
        help_text="Batch number for the product."
    )
    purchase_order_id = models.ForeignKey(  # Link inventory to purchase order
        PurchaseOrder,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text="Reference to the purchase order that supplied this inventory."
    )
    stock_in = models.IntegerField()  # Number of items added to inventory
    stock_out = models.IntegerField()  # Number of items removed from inventory
    expiration_date = models.DateField()  # Expiry date of the inventory
    stock_available = models.IntegerField()  # Current stock remaining
    low_stock_threshold = models.IntegerField()  # Threshold for low-stock warnings


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=500)

class Discount(models.Model):
    discount_id = models.AutoField(primary_key=True)
    discount_type = models.CharField(max_length=500)
    discount_amount = models.DecimalField(decimal_places=2, max_digits=10)

class Sales(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    invoice_date = models.DateField()
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    discount_id = models.ForeignKey(Discount, on_delete=models.PROTECT)
    net_total = models.DecimalField(decimal_places=2, max_digits=10)

class SalesDetails(models.Model):
    sales_details_id = models.AutoField(primary_key=True)
    invoice_id = models.ForeignKey(Sales, on_delete=models.PROTECT)
    customer_id = models.ForeignKey(Customer,on_delete=models.PROTECT,related_name="sales_details_customer")
    invoice_date = models.ForeignKey(Sales, on_delete=models.PROTECT, related_name="sales_details_invoice")  # Modify this as necessary (or remove if redundant)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)
    net_total = models.DecimalField(decimal_places=2, max_digits=10)

class ExpiredProduct(models.Model):
    expired_product_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)  # Product reference
    inventory_id = models.ForeignKey(Inventory, on_delete=models.PROTECT)  # Reference to the inventory
    expiry_date = models.DateField()  # Expiry date from inventory
    batch_number = models.CharField(max_length=100)  # Batch number from inventory
    base_price = models.DecimalField(max_digits=10, decimal_places=2)  # Base price
    is_replaced = models.BooleanField(  # Whether replaced or thrown away
        default=False,
        help_text="True if replaced by supplier, False if thrown away."
    )
    supplier_id = models.ForeignKey(Supplier, on_delete=models.PROTECT)  # Supplier that provided the product
    timestamp = models.DateTimeField(auto_now_add=True)  # Time of record creation
