from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Restaurant
from .forms import CommentForm


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


def restaurant_detail(request, slug):
    """
    This view is used to display the full restaurant details.
    """

    queryset = Restaurant.objects.filter(status=1)
    restaurant = get_object_or_404(queryset, slug=slug)
    comments = restaurant.comments.all().order_by("-created_on")
    comment_count = restaurant.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.restaurant = restaurant
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )
    comment_form = CommentForm()    


    return render(
        request,
        "restaurant_detail.html",
        {"restaurant": restaurant,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        }
    )
