from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('monitor/', views.monitor, name='monitor'),
    path('monitor/details/<int:id>', views.details, name='details'),
    path('events_help/', views.events_help, name='events_help'),
    path('search/', views.search, name='search')
]
