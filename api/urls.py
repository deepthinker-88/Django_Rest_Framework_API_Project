from django.contrib import admin 
from django.urls import path,include
from . import views
urlpatterns = [

path("",views.player_list),
path("player/<str:pk>",views.individual_player),
path("players/add",views.player_post),
path("player-update/<str:pk>",views.player_update),
path("player-delete/<str:pk>", views.delete_player),

]
