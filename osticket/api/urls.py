from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('tk_create', views.tk_create, name='tk_create'),
    path('list_topic', views.list_topic, name='list_topic'),
]