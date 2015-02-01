from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^first_prisoner$', views.first_prisoner, name='first_prisoner'),
    url(r'^second_prisoner$', views.second_prisoner, name='second_prisoner'),
    url(r'^results$', views.results, name='results'),
    url(r'^invalid_code$', views.results, name='invalid_code'),
)