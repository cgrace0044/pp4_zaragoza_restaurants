from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Restaurant, Comment
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
    queryset = Restaurant.objects.filter(status=1).order_by("-created_on")
    template_name = "browse_restaurants.html"
    paginate_by = 8


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
                request, messages.SUCCESS, "Comment submitted and awaiting approval"
            )
    comment_form = CommentForm()

    return render(
        request,
        "restaurant_detail.html",
        {
            "restaurant": restaurant,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":
        queryset = Restaurant.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("restaurant_detail", args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Restaurant.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("restaurant_detail", args=[slug]))
