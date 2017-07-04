from django.apps import AppConfig


class ControleConfig(AppConfig):
    name = 'controle'

admin.site.register(Config_Padrao)
admin.site.register(Log_Temperatura)
admin.site.register(Log_Luminosidade)
admin.site.register(Log_Irrigacao)