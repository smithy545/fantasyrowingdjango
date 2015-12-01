from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<team_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^page/(?P<page_id>[0-9]+)/$', views.team_page, name='page'),
    url(r'^page/(?P<last_page>[0-9]+)/$', views.team_page, name='page'),
    url(r'^edit/(?P<team_id>[0-9]+)/$', views.edit, name='edit'),
    ]
