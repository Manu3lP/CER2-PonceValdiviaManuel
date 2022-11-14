from django.db import models

# Create your models here.


class Recidencia(models.Model):
    nu_recidencia=models.IntegerField()
    n_correo=models.IntegerField()

    def _str_(self):
        return self.n_recidencia


class correos_M(models.Model):
    Paquete='caja'
    Documento='correo'
    T_CORREO=[(Paquete, 'paquete'),(Documento,'documentos')]
    id_correo=models.IntegerField()
    n_recidencia=models.IntegerField()
    Tipo_correo=models.CharField(max_length=20, choices=T_CORREO, default=Documento,)
    Mensaje=models.CharField(blank=True, null=True,max_length=300)
    
    def _str_(self):
        return self.id_correo
    