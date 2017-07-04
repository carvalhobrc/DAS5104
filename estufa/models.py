from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Estufa(models.Model):
    user = models.ManyToManyField(User)
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.nome

class Slot(models.Model):
    estufa = models.ForeignKey(Estufa, on_delete=models.CASCADE)
    numero = models.IntegerField(primary_key=True)
    planta = models.CharField(max_length=50, default='')
    sp_luz_intensidade = models.FloatField
    sp_luz_frequencia = models.FloatField
    sp_temp_min = models.FloatField
    sp_temp_max = models.FloatField
    sp_temp_ideal = models.FloatField
    sp_irrig_intervalo = models.FloatField
    sp_irrig_frequencia = models.FloatField = models.FloatField

    def __str__(self):
        return self.estufa + " - Slot " + self.numero
