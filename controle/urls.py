from django.conf.urls import *
from rest_framework import routers
from controle import views

router = routers.DefaultRouter()
router.register(r'controle', views.ControleViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]