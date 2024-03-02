from django.db import models

class Pedido(models.Model):
    fecha = models.DateField()
    direccion = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calcular el precio basado en la cantidad
        self.precio = self.cantidad * 10
        super().save(*args, **kwargs)
