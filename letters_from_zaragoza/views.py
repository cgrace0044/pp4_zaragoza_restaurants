from django.shortcuts import render
from django.views import generic
from .models import Restaurant


# Create your views here.
class Home(generic.TemplateView):
    """This view is used to display the home page"""

    template_name = "index.html"


class RestaurantList(generic.ListView):
    """
    Display a list of approved reviews

    """
    model = Restaurant
    queryset = Restaurant.objects.filter(status=1)
    template_name = "browse_restaurants.html"
    paginate_by = 6
