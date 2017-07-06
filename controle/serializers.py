from rest_framework import serializers
from controle.models import Log_Luminosidade, Log_Irrigacao, Log_Temperatura
from django.contrib.auth.models import User

class LogLuminosidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log_Luminosidade
        fields = ('datahora', 'intensidade', 'frequencia')

class LogIrrigacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log_Irrigacao
        fields = ('datahora', 'irrig_intervalo', 'irrig_freq')

class LogTemperaturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log_Temperatura
        fields = ('datahora', 'temperatura')

