from django.shortcuts import render
from django.views import generic
from .models import Restaurant


# Create your views here.
class Browse_Restaurants(generic.ListView):
    queryset = Restaurant.objects.filter(status=1)
    template_name = "browse_restaurants.html"

