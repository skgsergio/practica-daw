# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # Competiciones
    url(r'^competiciones/$',
        views.competiciones,
        name='competiciones'),
    url(r'^competiciones/(?P<pagina>[0-9]+)/$',
        views.competiciones,
        name='competiciones'),
    url(r'^competiciones/privadas/$',
        views.competiciones_privadas,
        name='competiciones_privadas'),
    url(r'^competiciones/privadas/(?P<pagina>[0-9]+)/$',
        views.competiciones_privadas,
        name='competiciones_privadas'),
    url(r'^competicion/(?P<id_competicion>[0-9]+)/$',
        views.competicion,
        name='competicion'),
    url(r'^competicion/(?P<id_competicion>[0-9]+)/(?P<pagina>[0-9]+)/$',
        views.competicion,
        name='competicion'),

    # Equipos
    url(r'^equipos/$',
        views.equipos,
        name='equipos'),
    url(r'^equipos/(?P<pagina>[0-9]+)/$',
        views.equipos,
        name='equipos'),
    url(r'^equipo/(?P<id_equipo>[0-9]+)/$',
        views.equipo,
        name='equipo'),
    url(r'^equipo/(?P<id_equipo>[0-9]+)/(?P<pagina>[0-9]+)/$',
        views.equipo,
        name='equipo'),

    # Jugadores
    url(r'^jugadores/$',
        views.jugadores,
        name='jugadores'),
    url(r'^jugadores/(?P<pagina>[0-9]+)/$',
        views.jugadores,
        name='jugadores'),
    url(r'^jugadores/(?P<posicion>po|df|ce|dl)/$',
        views.jugadores,
        name='jugadores'),
    url(r'^jugadores/(?P<posicion>po|df|ce|dl)/(?P<pagina>[0-9]+)/$',
        views.jugadores,
        name='jugadores'),
    url(r'^jugador/(?P<id_jugador>[0-9]+)/$',
        views.jugador,
        name='jugador'),
    url(r'^jugador/(?P<id_jugador>[0-9]+)/(?P<pagina>[0-9]+)/$',
        views.jugador,
        name='jugador'),
]
