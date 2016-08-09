from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^coaching/(?P<survey_code>.+)/$', views.coaching),
    url(r'^thanks', views.thanks),
    url(r'^survey', views.index, name='index'),
    url(r'^start', views.start),
    url(r'^$', views.start, name='index'),
]