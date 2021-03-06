# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.home,
        name='home'),

    # Usuarios
    url(r'^usuario/$',
        views.usuario,
        name='usuario'),
    url(r'^usuario/login/$',
        views.do_login,
        name='login'),
    url(r'^usuario/logout/$',
        views.do_logout,
        name='logout'),
    url(r'^usuario/registro/$',
        views.registro,
        name='registro'),

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

    # Partido
    url(r'^partido/(?P<id_partido>[0-9]+)/$',
        views.partido,
        name='partido'),

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

    # API para Javascript
    url(r'^get/equipos/$',
        views.get_equipos),
    url(r'^get/jugadores/(?P<id_partido>[0-9]+)/(?P<id_equipo>[0-9]+)/$',
        views.get_jugadores),
    url(r'^get/dorsales/(?P<id_equipo>[0-9]+)/$',
        views.get_dorsales),
    url(r'^get/partidos/(?P<id_competicion>[0-9]+)/(?P<jornada>[0-9]+)/$',
        views.get_partidos),
]
