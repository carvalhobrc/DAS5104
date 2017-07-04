from django.shortcuts import render_to_response
from rest_framework import viewsets
from controle.serializers import LogLuminosidadeSerializer
from controle.models import Log_Luminosidade

# Create your views here.
class ControleViewSet(viewsets.ModelViewSet):
    queryset = Log_Luminosidade.objects.all()
    serializer_class = LogLuminosidadeSerializer