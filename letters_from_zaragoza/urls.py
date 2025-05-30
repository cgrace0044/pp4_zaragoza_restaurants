from . import views
from django.urls import path

urlpatterns = [
    path('', views.Browse_Restaurants.as_view(), name='restaurants'),
]