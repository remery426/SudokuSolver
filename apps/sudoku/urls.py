from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'change/(?P<id>\d*)$',views.change),
    url(r'changeval/(?P<id>\d*)$',views.changeval),
    url(r'clear$',views.clear),
    url(r'solve$',views.solve)
]
