from django.shortcuts import render_to_response
from rest_framework import viewsets
from estufa.serializers import EstufaSerializer, SlotSerializer
from estufa.models import Estufa, Slot

# Create your views here.
class EstufaViewSet(viewsets.ModelViewSet):
    queryset = Estufa.objects.all()
    serializer_class = EstufaSerializer

class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer