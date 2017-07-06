from django.conf.urls import *
from rest_framework import routers
from controle import views

routerLuminosidade = routers.DefaultRouter()
routerLuminosidade.register(r'luminosidade', views.LuminosidadeViewSet)

routerIrrigacao = routers.DefaultRouter()
routerIrrigacao.register(r'irrigacao', views.IrrigacaoViewSet)

routerTemperatura = routers.DefaultRouter()
routerTemperatura.register(r'temperatura', views.TemperaturaViewSet)

urlpatterns = [
    url(r'^luminosidade_api/', include(routerLuminosidade.urls)),
    url(r'^irrigacao_api/', include(routerIrrigacao.urls)),
    url(r'^temperatura_api/', include(routerTemperatura.urls)),
]