from rest_framework import serializers
from controle.models import Log_Luminosidade
from django.contrib.auth.models import User

class LogLuminosidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log_Luminosidade
        fields = ('datahora', 'intensidade', 'frequencia')

