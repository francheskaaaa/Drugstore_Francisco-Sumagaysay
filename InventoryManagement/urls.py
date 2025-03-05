from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from DrugstoreApp import views  # Import views from the current app
from DrugstoreApp.views import UserNameViewSet

router = routers.DefaultRouter()
router.register('user', views.UserViewSet,basename='user')
router.register('auditLog',views.AuditLogViewSet,basename='auditLog')
router.register('report', views.ReportViewSet,basename='report')
router.register('category', views.CategoryViewSet,basename='category')
router.register('supplier', views.SupplierViewSet,basename='supplier')
router.register('product', views.ProductViewSet,basename='product')
router.register('purchaseOrder', views.PurchaseOrderViewSet, basename='purchaseOrder')
router.register('inventory', views.InventoryViewSet, basename='inventory')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/gettoken/', TokenObtainPairView.as_view(), name='gettoken'),
    path('api/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/userbyname/<str:name>/', UserNameViewSet.as_view(), name='companybyname'),

]
