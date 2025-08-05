from django.urls import path
from .views import *
urlpatterns = [
    path('sign_up/', v_sign_up, name='sign_up'),
    path('login/',v_login,name='log_in'),
    path('logout/', v_logout, name='log_out'),
]