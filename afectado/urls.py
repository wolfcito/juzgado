from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.inicio),
        url(r'^afectado/$', views.lista_afectados),
        url(r'^afectado/(?P<id>[0-9]+)/$', views.detalle_afectado),
        url(r'^afectado/nuevo/$', views.nuevo_afectado, name='nuevo_afectado'),
        url(r'^afectado/(?P<id>[0-9]+)/edit/$', views.editar_afectado, name='editar_afectado'),
]