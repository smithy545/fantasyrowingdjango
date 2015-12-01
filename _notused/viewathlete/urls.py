from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='viewathlete:index'),
    url(r'^(?P<rower_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^page/(?P<page_id>[0-9]+)/$', views.rower_page, name='page'),
    url(r'^page/(?P<next_page>[0-9]+)/$', views.rower_page, name='page'),
    url(r'^page/(?P<last_page>[0-9]+)/$', views.rower_page, name='page'),
    ]
