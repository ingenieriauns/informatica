from django.urls import path

from marcador import views

urlpatterns = [
    path('', views.bookmark_list, name='bookmark_list' ),
    path('bookmark_list/', views.bookmark_list, name='bookmark_list' ),
]