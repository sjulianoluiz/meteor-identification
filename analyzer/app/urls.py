from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="principal"),
  path('duvidosos', views.duvidosos, name="duvidosos"),
  path('configuracoes', views.configuracoes, name="configuracoes"),
  path('finalizar', views.finalizar, name="finalizar")
]
