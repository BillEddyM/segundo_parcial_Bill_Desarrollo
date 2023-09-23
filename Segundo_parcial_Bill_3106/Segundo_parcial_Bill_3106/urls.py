
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("customauthentication.urls")),
    path('', include("home.urls")),
    path('proveedores/', include("proveedor.urls")),
]
