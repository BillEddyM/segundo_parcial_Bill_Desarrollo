from django.urls import path
from .views import ProveedorListView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView

urlpatterns = [
    path('', ProveedorListView.as_view(), name='proveedor_list'),
    path('create/', ProveedorCreateView.as_view(), name='proveedor_create'),
    path('<int:pk>/update/', ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('<int:pk>/delete/', ProveedorDeleteView.as_view(), name='proveedor_delete'),
]
