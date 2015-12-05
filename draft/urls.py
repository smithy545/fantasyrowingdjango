from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
	url(r'^getathletes', views.league_get_available, name='league_get_available'),
	url(r'^getplayers', views.league_get_players, name='league_get_players'),
]
