from django.db import models
from estufa.models import Estufa, Slot

# Create your models here.
class Config_Padrao(models.Model):
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

class Log_Temperatura(models.Model):
    estufa = models.ForeignKey(Estufa, on_delete=models.CASCADE)
    datahora = models.DateTimeField(auto_now=True)
    temperatura = models.FloatField

    def __str__(self):
        return self.estufa + ":" + self.datahora + ":" + self.temperatura

class Log_Irrigacao(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    datahora = models.DateTimeField(auto_now=True)
    irrig_intervalo = models.FloatField
    irrig_freq = models.FloatField

    def __str__(self):
        return self.estufa + ":" + self.datahora

class Log_Luminosidade(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    datahora = models.DateTimeField(auto_now=True)
    intensidade = models.FloatField
    frequencia = models.FloatField

    def __str__(self):
        return self.estufa + ":" + self.datahora