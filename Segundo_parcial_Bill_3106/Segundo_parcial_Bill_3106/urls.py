
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers, filters

from proveedor.views import ProveedorViewSet

router = routers.DefaultRouter()
router.register(r'proveedores', ProveedorViewSet)

router.filter_backends = [filters.SearchFilter]
router.search_fields = ['nombre', 'id'] 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("customauthentication.urls")),
    path('', include("home.urls")),
    path('proveedores/', include("proveedor.urls")),
    path('api/', include(router.urls)),
]
