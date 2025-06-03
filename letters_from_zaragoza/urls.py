from . import views
from django.urls import path

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path('browse_restaurants/', views.RestaurantList.as_view(), name="browse_restaurants"),
]
