from django.contrib import admin
from core.models import correos_M, Recidencia
# Register your models here.
 
class CorreoAdmin(admin.ModelAdmin):
    list_display=("n_recidencia","Tipo_correo", "id_correo")
    search_fields=("n_recidencia", "id_correo")

class RecidenciaAdmin(admin.ModelAdmin):
    list_display=("nu_recidencia", "n_correo")
    search_fields=("nu_recidencia", "n_correo")

admin.site.register(correos_M, CorreoAdmin)
admin.site.register(Recidencia,RecidenciaAdmin)