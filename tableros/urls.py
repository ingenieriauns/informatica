from django.urls import path
from django.conf.urls import url

from tableros import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),
    url(r'(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
]