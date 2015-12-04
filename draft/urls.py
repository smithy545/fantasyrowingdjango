from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
	url(r'^get_athletes', views.league_get_available, name='league_get_available'),

]
