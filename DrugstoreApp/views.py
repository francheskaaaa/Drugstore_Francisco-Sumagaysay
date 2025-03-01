from django.shortcuts import render, get_object_or_404
from git.objects.util import get_object_type_by_name
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from DrugstoreApp import models
from .models import User
from DrugstoreApp.models import User, Report, AuditLog, Category, Supplier, Product, Inventory, PurchaseOrder, \
    PurchaseOrderDetails, Customer, Discount, Sales, SalesDetails, ExpiredProduct
from .serializers import UserSerializer, ReportSerializer, AuditLogSerializer, ProductSerializer, CategorySerializer, \
    SupplierSerializer, PurchaseOrderSerializer, PurchaseOrderDetailsSerializer, PurchaseOrderDetailsSerializerSimple


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ViewSet):
    authenticated_users = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @staticmethod
    def list(request):
        users =User.objects.all()
        serializer=UserSerializer(users,many=True,context={'request': request})
        response_dict={"error":False,"message": "All User List Data", "data":serializer.data}
        return Response(response_dict)

    @staticmethod
    def create(request):
        serializer = UserSerializer(data=request.data,context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict = {"error":False,"message": "User Created Successfully"}
        else:
            response_dict = {"error":True,"message": "User Not Created"}

        return Response(response_dict)

    @staticmethod
    def update(request, pk=None):
        queryset = User.objects.all()
        users = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(users, data=request.data,context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict= {"error":False,"message": "User Updated Successfully"}
        else:
            response_dict = {"error":True,"message": "Error Updating User Data"}

        return Response(response_dict)

class UserNameViewSet(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        # Fetch the name from the 'name' parameter in the URL
        name = self.kwargs.get("name", "")  # Default to an empty string if not found
        # Ensure the name is not empty
        if not name:
            return User.objects.none()

        split_name = name.split()  # Split the name into parts
        # Check if the name has at least a first name and a last name
        if len(split_name) < 2:
            return User.objects.none()  # Return an empty queryset for invalid input

        # Filter by first name and last name
        first_name = split_name[0]
        last_name = " ".join(split_name[1:])  # Handle potential multi-part last names

        return User.objects.filter(first_name=first_name, last_name=last_name)

class AuditLogViewSet(viewsets.ViewSet):
    authenticated_users = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def list(request):
        audit_log = AuditLog.objects.all()
        serializer = AuditLogSerializer(audit_log, many=True, context={'request': request})
        response_dict = {"error": False, "message": "All Audit Log List Data", "data": serializer.data}
        return Response(response_dict)

    @staticmethod
    def create(request):
        serializer = AuditLogSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict = {"error": False, "message": "Audit Log Created Successfully"}
        else:
            response_dict = {"error": True, "message": "Audit Log Not Created"}

        return Response(response_dict)

    @staticmethod
    def retrieve(request, pk=None):
        queryset=AuditLog.objects.all()
        audit_log=get_object_or_404(queryset,pk=pk)
        serializer=AuditLogSerializer(audit_log,context={'request':request})
        return Response({"error": False,"message":"Single Data Fetch","data": serializer.data})

    @staticmethod
    def update(request, pk=None):
        queryset = AuditLog.objects.all()
        audit_log = get_object_or_404(queryset, pk=pk)
        serializer = AuditLogSerializer(audit_log, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict = {"error": False, "message": "Audit Log Data has been Updated Successfully"}
        else:
            response_dict = {"error": True, "message": "Error Updating Audit Log Data"}

        return Response(response_dict)


class ReportViewSet(viewsets.ViewSet):
    authenticated_users = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def list(request):
        report = Report.objects.all()
        serializer = ReportSerializer(report, many=True, context={'request': request})
        response_dict = {"error": False, "message": "All Report List Data", "data": serializer.data}
        return Response(response_dict)

    @staticmethod
    def create(request):
        serializer = ReportSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict = {"error": False, "message": "Report Created Successfully"}
        else:
            response_dict = {"error": True, "message": "Report Not Created"}

        return Response(response_dict)

    # queryset = Report.objects.select_related('user_id').all()  # Optimize for user querying
    # serializer_class = ReportSerializer

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     for report in qs:  # Debugging each report
    #         print(f"Report ID: {report.report_id}, User ID: {report.user_id}")
    #     return qs

    @staticmethod
    def retrieve(request, pk=None):
        queryset=Report.objects.all()
        report=get_object_or_404(queryset,pk=pk)
        serializer=ReportSerializer(report,context={'request':request})
        return Response({"error": False,"message":"Single Data Fetch","data": serializer.data})

    @staticmethod
    def update(request, pk=None):
        queryset = Report.objects.all()
        report = get_object_or_404(queryset, pk=pk)
        serializer = ReportSerializer(report, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict = {"error": False, "message": "Report Data has been Updated Successfully"}
        else:
            response_dict = {"error": True, "message": "Error Updating Report Data"}

        return Response(response_dict)

class CategoryViewSet(viewsets.ViewSet):
    authenticated_users = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def list(request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True, context={'request': request})
        response_dict = {"error": False, "message": "All Category List Data", "data": serializer.data}
        return Response(response_dict)

    @staticmethod
    def create(request):
        serializer = CategorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict = {"error": False, "message": "Product Category Created Successfully"}
        else:
            response_dict = {"error": True, "message": "Product Category Not Created"}

        return Response(response_dict)

    @staticmethod
    def retrieve(request, pk=None):
        queryset=Category.objects.all()
        category=get_object_or_404(queryset,pk=pk)
        serializer=CategorySerializer(category,context={'request':request})
        return Response({"error": False,"message":"Single Data Fetch","data": serializer.data})

    @staticmethod
    def update(request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict = {"error": False, "message": "Product Category Data has been Updated Successfully"}
        else:
            response_dict = {"error": True, "message": "Error Updating Product Category Data"}

        return Response(response_dict)

class SupplierViewSet(viewsets.ViewSet):
    authenticated_users = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def list(request):
        supplier = Supplier.objects.all()
        serializer = SupplierSerializer(supplier, many=True, context={'request': request})
        response_dict = {"error": False, "message": "All Supplier List Data", "data": serializer.data}
        return Response(response_dict)

    @staticmethod
    def create(request):
        serializer = SupplierSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict = {"error": False, "message": "Supplier Created Successfully"}
        else:
            response_dict = {"error": True, "message": "Supplier Not Created"}

        return Response(response_dict)

    @staticmethod
    def retrieve(request, pk=None):
        queryset=Supplier.objects.all()
        supplier=get_object_or_404(queryset,pk=pk)
        serializer=SupplierSerializer(supplier,context={'request':request})
        return Response({"error": False,"message":"Single Data Fetch","data": serializer.data})

    @staticmethod
    def update(request, pk=None):
        queryset = Supplier.objects.all()
        supplier = get_object_or_404(queryset, pk=pk)
        serializer = SupplierSerializer(supplier, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict = {"error": False, "message": "Supplier Data has been Updated Successfully"}
        else:
            response_dict = {"error": True, "message": "Error Updating Supplier Data"}

        return Response(response_dict)

class ProductViewSet(viewsets.ViewSet):
    authenticated_users = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def list(request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True, context={'request': request})
        response_dict = {"error": False, "message": "All Product List Data", "data": serializer.data}
        return Response(response_dict)

    @staticmethod
    def create(request):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict = {"error": False, "message": "Product Created Successfully"}
        else:
            response_dict = {"error": True, "message": "Product Not Created"}

        return Response(response_dict)

    @staticmethod
    def retrieve(request, pk=None):
        queryset=Product.objects.all()
        product=get_object_or_404(queryset,pk=pk)
        serializer=ProductSerializer(product,context={'request':request})
        return Response({"error": False,"message":"Single Data Fetch","data": serializer.data})

    @staticmethod
    def update(request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict = {"error": False, "message": "Product Data has been Updated Successfully"}
        else:
            response_dict = {"error": True, "message": "Error Updating Product Data"}

        return Response(response_dict)

class PurchaseOrderViewSet(viewsets.ViewSet):
    authenticated_users = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def list(request):
        purchase_order = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_order, many=True, context={'request': request})

        purchase_order_data=serializer.data
        new_purchase_order_list=[]

        #add extra key for purchase order details in purchase order
        for purchase_order in purchase_order_data:
            #access all purchase details of current purchase id
            purchase_order_details=PurchaseOrderDetails.objects.filter(purchase_order_id=purchase_order['purchase_order_id'])
            purchase_order_details_serializers=PurchaseOrderDetailsSerializerSimple(purchase_order_details,many=True,context={'request':request})
            purchase_order["purchase_order_details"]=purchase_order_details_serializers.data
            new_purchase_order_list.append(purchase_order)

        response_dict = {"error": False, "message": "All Purchase Order List Data", "data": serializer.data}
        return Response(response_dict)

    @staticmethod
    def create(request):
        serializer = PurchaseOrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            purchase_order_id=serializer.data['purchase_order_id']

            #access the serializer id saved on the db
            # print(purchase_order_id)

            #adding and saving id to purchase order details table
            purchase_order_details_list=[]
            for purchase_order_details in request.data['purchase_order_details']:
                #print(purchase_order_details)

                #adding purchase order id to work on purchase order details serializer
                purchase_order_details["purchase_order_id"]=purchase_order_id
                purchase_order_details_list.append(purchase_order_details)
                print(purchase_order_details_list)

            serializer2=PurchaseOrderDetailsSerializer(data=purchase_order_details_list,many=True,context={'request':request})
            if serializer2.is_valid(raise_exception=True):
                serializer2.save()

            response_dict = {"error": False, "message": "Purchase Order Created Successfully"}
        else:
            response_dict = {"error": True, "message": "Purchase Order Not Created"}

        return Response(response_dict)

    @staticmethod
    def retrieve(request, pk=None):
        queryset=PurchaseOrder.objects.all()
        purchase_order=get_object_or_404(queryset,pk=pk)
        serializer=PurchaseOrderSerializer(purchase_order,context={'request':request})

        serializer_data=serializer.data

        #access all purchase details of current purchase id
        purchase_order_details=PurchaseOrderDetails.objects.filter(purchase_order_id=serializer_data['purchase_order_id'])
        purchase_order_details_serializers=PurchaseOrderDetailsSerializerSimple(purchase_order_details,many=True,context={'request':request})
        serializer_data["purchase_order_details"]=purchase_order_details_serializers.data

        return Response({"error": False,"message":"Single Data Fetch","data":serializer_data })

    @staticmethod
    def update(request, pk=None):
        queryset = PurchaseOrder.objects.all()
        purchase_order = get_object_or_404(queryset, pk=pk)
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_dict = {"error": False, "message": "Purchase Order Data has been Updated Successfully"}
        else:
            response_dict = {"error": True, "message": "Error Updating Purchase Order Data"}

        return Response(response_dict)

user_list=UserViewSet.as_view({'get':'list'})
user_create=UserViewSet.as_view({'post':'create'})
user_update=UserViewSet.as_view({'put':'update'})


