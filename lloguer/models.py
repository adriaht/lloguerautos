from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)


class Reserva(models.Model):
    automobil = models.ForeignKey(Automobil, on_delete=models.CASCADE)  # Relación con el automóvil
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    fecha_inicio = models.DateTimeField()  # Fecha de inicio del alquiler
    fecha_fin = models.DateTimeField()  # Fecha de fin del alquiler
    creado_en = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la reserva

    class Meta:
        unique_together = ('automobil', 'fecha_inicio')  # No se puede alquilar el mismo coche el mismo día


    def __str__(self):
        return f"{self.usuario.username} - {self.automobil.marca} {self.automobil.model} ({self.fecha_inicio} - {self.fecha_fin})"