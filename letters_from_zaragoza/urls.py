from . import views
from django.urls import path

urlpatterns = [
    path('browse_restaurants/', views.Browse_Restaurants.as_view(), name='restaurants'),
]