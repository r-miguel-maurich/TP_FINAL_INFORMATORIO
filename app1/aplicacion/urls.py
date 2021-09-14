from django.urls import path
from . import views
from aplicacion.views import Index

urlpatterns = [
    path('',views.hola, name='hola'),
#    path('Listar/', views.Listar.as_view(), name="listar")
#    path('', views.Index.as_view(), name='inde'),
    path('indexx/',Index.as_view(), name='indice'),
]
