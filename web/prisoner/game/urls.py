from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^results$', views.results, name='results'),
    url(r'^invalid_code$', views.results, name='invalid_code'),
)