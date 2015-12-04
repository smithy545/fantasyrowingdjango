from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^about', views.AboutView.as_view(), name='about'),
	url(r'^maketeam/success', views.TeamSuccessView.as_view(), name='make_team_success'),
	url(r'^newleague/success', views.LeagueSuccessView.as_view(), name='make_league_success'),
    url(r'^team/(?P<team_id>[0-9]+)/$', views.team_detail, name='team_detail'),
    url(r'^team', views.my_team_detail, name='my_team_detail'),
    url(r'^(?P<page_id>[0-9]+)/$', views.team_page, name='team_page'),
	url(r'^editteam/add/(?P<athlete_id>[0-9]+)/$', views.athlete_add, name='athlete_add'),
	url(r'^editteam/remove/(?P<athlete_id>[0-9]+)/$', views.athlete_remove, name='athlete_remove'),
	url(r'^editname', views.team_edit_name, name='team_edit_name'),
	url(r'^addathlete', views.team_add_athlete, name='team_add_athlete'),
	url(r'^removeathlete', views.team_remove_athlete, name='team_remove_athlete'),
	url(r'^get_athletes(.)*', views.team_get_athletes, name='team_athlete_get'),
	url(r'^tradeathlete', views.team_trade_athlete, name='team_trade_athlete'),
    url(r'^signin', views.sign_in, name='sign_in'),
    url(r'^signout', views.sign_out, name='sign_out'),
	url(r'^athlete/(?P<athlete_id>[0-9]+)/$', views.athlete_detail, name='athlete_detail'),
	url(r'^signup', views.sign_up, name='sign_up'),
	url(r'^league/(?P<league_id>[0-9]+)/$', views.league_detail, name='league_detail'),
	url(r'^league', views.my_league_detail, name='my_league_detail'),
	url(r'^editleague', views.league_edit, name='league_edit'),
	url(r'^kickuser/(?P<user_id>[0-9]+)/$', views.league_kick_user, name='league_kick_user'),
	url(r'^maketeam', views.make_team, name='make_team'),
	url(r'^newleague', views.new_league, name='new_league'),
    ]
