from django.contrib import admin

from .models import Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'direccion']
    list_display = ['id', 'nombre', 'direccion']
    list_filter = ['nombre', 'id']
    actions = ['delete_selected']
    
    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, "Los proveedores seleccionados han sido eliminados.")
    delete_selected.short_description = "Eliminar proveedores seleccionados"

admin.site.register(Proveedor, ProveedorAdmin)

