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
from natura.views import (index, about, ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete, SignUp, Login, Logout, ProfileUpdate, ProfileCreate, ProfileDelete, ProfileList, ProfileDetail, MensajeCreate, MensajeDelete, MensajeList)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('productos/list', ProductList.as_view(), name='productos-list'),
    path('productos/<pk>/detail', ProductDetail.as_view(), name='productos-detail'),
    path('productos/create', ProductCreate.as_view(), name='productos-create'),
    path('productos/<pk>/update', ProductUpdate.as_view(), name='productos-update'),
    path('productos/<pk>/delete', ProductDelete.as_view(), name='productos-delete'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/list', ProfileList.as_view(), name='profile-list'),
    path('profile/<pk>/detail', ProfileDetail.as_view(), name='profile-detail'),
    path('profile/create', ProfileCreate.as_view(), name='profile-create'),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name='profile-update'),
    path('profile/<pk>/delete', ProfileDelete.as_view(), name='profile-delete'),
    path('mensaje/enviar', MensajeCreate.as_view(), name='mensaje-enviar'),
    path('mensaje/list', MensajeList.as_view(), name='mensaje-list'),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name='mensaje-delete'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)