from django.db import models

class Casa(models.Model):
    ESTADO_CHOICES = [
        ('Renta', 'Renta'),
        ('Venta', 'Venta'),
    ]

    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Venta')
    habitaciones = models.IntegerField()

    def __str__(self):
        return f'{self.direccion}, {self.ciudad} ({self.estado})'
# Create your models here.
