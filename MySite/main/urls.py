from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('db', views.db, name = 'db'),
    path('makedb', views.makedb, name = 'makedb'),
]