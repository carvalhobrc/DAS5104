from django.contrib import admin
from controle.models import Config_Padrao, Log_Irrigacao, Log_Luminosidade, Log_Temperatura

# Register your models here.
admin.site.register(Config_Padrao)
admin.site.register(Log_Luminosidade)
admin.site.register(Log_Temperatura)
admin.site.register(Log_Irrigacao)
