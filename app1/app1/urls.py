"""app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aplicacion.views import Index, Home, Login, Home, Crear, Listar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aplicacion', include('aplicacion.urls')),
#    path('', views.index, name='index'),
    path('index1/',Index.as_view(), name='indice'),
    path('home/',Home.as_view(), name='inicio'),
    path('login/',Login.as_view(), name='logeo'),
    path('crear/',Crear.as_view(), name=''),
    path('listar/',Listar.as_view(), name=''),
]
