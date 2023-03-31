"""mi_primer_mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from natura.views import index, mostrar_mis_productos, cargar_producto, BuscarProducto, cargar_consultora, BuscarConsultora, cargar_cliente, BuscarCliente


urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('mis-productos/', mostrar_mis_productos, name="mis-productos"),
    path('mis-productos/create', cargar_producto, name="mis-productos-create"),
    path('mis-productos/list', BuscarProducto.as_view(), name='productos-list'),
    path('consultoras/create', cargar_consultora, name="consultoras-create"),
    path('consultoras/list', BuscarConsultora.as_view(), name='consultoras-list'),
    path('mis-clientes/create', cargar_cliente, name="mis-clientes-create"),
    path('mis-clientes/list', BuscarCliente.as_view(), name='clientes-list'),
]
