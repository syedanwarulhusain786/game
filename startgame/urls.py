# from .views import RegisterAPI
from django.urls import path
from .views import *

from . import views
# from django.contrib.auth import views as auth_views

# from django.utils.translation import gettext as _


# from django.urls import path,include



urlpatterns = [

    path('', views.home, name='home'),
    path('get_player_data/', views.get_player_data, name='get_player_data'),
    path('start_game/', views.start_game, name='start_game'),
    path('reset_game/', views.reset_game, name='reset_game'),
    
    


   
]