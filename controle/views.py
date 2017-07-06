from django.shortcuts import render_to_response
from rest_framework import viewsets
from controle.serializers import LogLuminosidadeSerializer, LogIrrigacaoSerializer, LogTemperaturaSerializer
from controle.models import Log_Luminosidade, Log_Temperatura, Log_Irrigacao

# Create your views here.
class LuminosidadeViewSet(viewsets.ModelViewSet):
    queryset = Log_Luminosidade.objects.all()
    serializer_class = LogLuminosidadeSerializer

class IrrigacaoViewSet(viewsets.ModelViewSet):
    queryset = Log_Irrigacao.objects.all()
    serializer_class = LogIrrigacaoSerializer

class TemperaturaViewSet(viewsets.ModelViewSet):
    queryset = Log_Temperatura.objects.all()
    serializer_class = LogTemperaturaSerializer