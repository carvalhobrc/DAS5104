from rest_framework import serializers
from estufa.models import Estufa, Slot
from django.contrib.auth.models import User

class EstufaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estufa
        fields = ('nome', 'codigo')

class SlotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slot
        fields = ('estufa', 'numero', 'planta')