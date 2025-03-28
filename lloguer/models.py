from django.db import models
from django.contrib.auth.models import User


class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.matricula}"


class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    automobil = models.ForeignKey(Automobil, on_delete=models.CASCADE)  
    data_inicio = models.DateTimeField() 
    data_fi = models.DateTimeField()  

    class Meta:
        unique_together = ('automobil', 'data_inicio') 

    def __str__(self):
        return f"Reserva de {self.automobil} por {self.user} desde {self.data_inicio} hasta {self.data_fi}"