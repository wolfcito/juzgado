from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.lista_afectados),
        url(r'^afectado/(?P<id>[0-9]+)/$', views.detalle_afectado),
]