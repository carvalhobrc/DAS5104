from django.conf.urls import *
from rest_framework import routers
from estufa import views

routerEstufa = routers.DefaultRouter()
routerEstufa.register(r'estufa', views.EstufaViewSet)

routerSlot = routers.DefaultRouter()
routerSlot.register(r'slot', views.SlotViewSet)

urlpatterns = [
    url(r'^estufa_api/', include(routerEstufa.urls)),
    url(r'^slot_api/', include(routerSlot.urls)),
]