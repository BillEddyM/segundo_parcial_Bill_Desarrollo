from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Proveedor
from .forms import ProveedorForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy  #PARA EL REDIRECCIONAMIENTO AUTOMATICO

#imports necesarias para la api 
from rest_framework import viewsets
from .serializers import ProveedorSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

class ProveedorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Proveedor
    template_name = 'proveedor/proveedor_list.html'
    context_object_name = 'proveedores'
    permission_required = 'proveedor.view_proveedor'
    

class ProveedorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')
    permission_required = 'proveedor.add_proveedor'

class ProveedorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')
    permission_required = 'proveedor.change_proveedor'

class ProveedorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Proveedor
    template_name = 'proveedor/proveedor_confirm_delete.html' #direccion del template 
    success_url = reverse_lazy('proveedor_list') #para redireccionar automaticamente reverse lazy 
    permission_required = 'proveedor.delete_proveedor'


#Vista api 

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    pagination_class = PageNumberPagination  # Agregar el paginador
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'id'] 

