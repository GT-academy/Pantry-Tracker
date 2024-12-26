from django.db import models
from django.utils.timezone import now

class Item(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_caducidad = models.DateField()
    usado = models.BooleanField(default=False)

    def dias_restantes(self):
        return (self.fecha_caducidad - now().date()).days

    def esta_por_caducar(self):
        return self.dias_restantes() <= 3  # Ejemplo: 3 días antes

    def __str__(self):
        return f"{self.nombre} ({self.cantidad})"

