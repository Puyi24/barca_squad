from django.urls import path
from . import views
app_name = 'players'
urlpatterns = [
    path('add-player/', views.add_player, name='add_player'),
    path('<slug:slug>/', views.player_details, name='details')
]
