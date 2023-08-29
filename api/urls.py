from django.contrib import admin 
from django.urls import path,include
#from api.views import PlayersViewSet
from . import views
# from rest_framework.routers import DefaultRouter 

# router = DefaultRouter()

# router.register("",PlayersViewSet,basename="players")


urlpatterns = [
# Below are views using router
#path('admin/',admin.site.urls),
#path('players/',include(router.urls))

# Below are views using viewset
#path("",views.PlayersViewSet.as_view({'create':'list'})),
# path("",views.PlayersViewSet.as_view({'get':'list'})),
# path("<int:pk>",views.PlayersViewSet.as_view({'get':'retrieve'})),
# path("<int:pk>",views.PlayersViewSet.as_view({'update':'update'}))

# Below are views using generic based views and mixins
# path("",views.PlayersListCreateView.as_view()),
# path("<int:pk>",views.PostRetrieveUpdateDeleteView.as_view())

# Below are class based views
#path("",views.PlayersListCreateView.as_view(),name = "list_players"), 
# path("player-update/<str:pk>",views.PlayersRetrieveUpdateDestroyView.as_view(),name= "update_players"),
# path("player-delete/<str:pk>",views.PlayersRetrieveUpdateDestroyView.as_view())

#These are function based views below
path("",views.player_list),
path("player/<str:pk>",views.individual_player),
path("players/add",views.player_post),
path("player-update/<str:pk>",views.player_update),
path("player-delete/<str:pk>", views.delete_player),

]
