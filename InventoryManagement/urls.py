from django.contrib import admin
from django.urls import path
from DrugstoreApp import views  # Import views from the current app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),  # Connects 'login/' to login_view
    path('home/', views.home_view, name='home'),
    path('inventory/', views.inventory_view, name='inventory'),
    path('product/', views.product_view, name='product'),
    path('customer/', views.customer_view, name='customer'),
    path('sales/', views.sales_view, name='sales'),
    path('supplier/', views.supplier_view, name='supplier'),
    path('user/', views.user_view, name='user'),
    path('report/', views.report_view, name='report'),
    path('auditlog/', views.auditlog_view, name='auditlog'),
    path('create/', views.create_view, name='create'),


]
