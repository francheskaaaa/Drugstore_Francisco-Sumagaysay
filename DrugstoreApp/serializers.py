from rest_framework import serializers

from DrugstoreApp.models import User, Report, AuditLog, Category, Supplier, Product, Inventory, PurchaseOrder, \
    PurchaseOrderDetails, Customer, Discount, Sales, SalesDetails, ExpiredProduct


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields="__all__"

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=AuditLog
        fields="__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        # Pass the serializer context (containing the request) to the nested UserSerializer
        response['users'] = UserSerializer(instance.user_id, context=self.context).data

        return response

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        # Pass the serializer context (containing the request) to the nested UserSerializer
        response['users'] = UserSerializer(instance.user_id, context=self.context).data

        return response

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        # Pass the serializer context (containing the request) to the nested UserSerializer
        response['category'] = CategorySerializer(instance.category_id, context=self.context).data
        response['supplier'] = SupplierSerializer(instance.supplier_id, context=self.context).data

        return response



class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        # Pass the serializer context (containing the request) to the nested SupplierSerializer
        response['supplier'] = SupplierSerializer(instance.supplier_id, context=self.context).data

        return response

class PurchaseOrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderDetails
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        # Pass the serializer context (containing the request) to the nested purchaseOrder and Product Serializer
        response['purchaseOrder'] = PurchaseOrderSerializer(instance.purchase_order_id, context=self.context).data
        response['product'] = ProductSerializer(instance.product_id, context=self.context).data

        return response

class PurchaseOrderDetailsSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderDetails
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        # Pass the serializer context (containing the request) to the nested purchaseOrder and Product Serializer
        response['product'] = ProductSerializer(instance.product_id, context=self.context).data

        return response

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        # Pass the serializer context (containing the request) to the nested ProductSerializer
        response['product'] = ProductSerializer(instance.product_id, context=self.context).data
        response['purchaseOrder'] = PurchaseOrderSerializer(instance.purchase_order_id, context=self.context).data
        return response

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        # Pass the serializer context (containing the request) to the nested Customer and Discount Serializer
        response['customer'] = CustomerSerializer(instance.customer_id, context=self.context).data
        response['discount'] = DiscountSerializer(instance.discount_id, context=self.context).data

        return response

class SalesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDetails
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        # Nested serializers for ForeignKey relationships
        response['sales'] = SalesSerializer(instance.invoice_id, context=self.context).data
        response['customer'] = CustomerSerializer(instance.customer_id, context=self.context).data
        response['product'] = ProductSerializer(instance.product_id, context=self.context).data

        # Nested serializer for another ForeignKey (invoice_date from Sales table)
        response['invoice_date'] = SalesSerializer(instance.invoice_date, context=self.context).data

        return response

class ExpiredProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiredProduct
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        # Nested serializers for ForeignKey relationships
        response['product'] = ProductSerializer(instance.product_id, context=self.context).data
        response['inventory'] = InventorySerializer(instance.inventory_id, context=self.context).data
        response['supplier'] = ProductSerializer(instance.supplier_id, context=self.context).data
        return response


