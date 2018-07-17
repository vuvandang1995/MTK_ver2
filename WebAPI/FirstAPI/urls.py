from django.urls import path
from . import views

app_name = 'FirstAPI'
urlpatterns = [
    path('user_list', views.user_list, name='user_list'),
    path('create_ticket', views.create_ticket, name='create_ticket'),
]