from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('monitor/', views.monitor, name='monitor'),
    path('monitor/details/<int:id>', views.details, name='details'),
    path('help/', views.help, name='help'),
    path('search/', views.search, name='search')
]