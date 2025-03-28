from django.db import models
from django.contrib.auth.models import User


class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.matricula}"


class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con User
    automobil = models.ForeignKey(Automobil, on_delete=models.CASCADE)  # Relación con Automobil
    data_inicio = models.DateTimeField()  # Fecha de inicio del alquiler
    data_fi = models.DateTimeField()  # Fecha de fin del alquiler

    class Meta:
        unique_together = ('automobil', 'data_inicio')  # Restricción de unicidad

    def __str__(self):
        return f"Reserva de {self.automobil} por {self.user} desde {self.data_inicio} hasta {self.data_fi}"