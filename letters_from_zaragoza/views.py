from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Restaurant, Comment
from .forms import CommentForm


# Create your views here.
class Home(generic.TemplateView):
    """View for rendering the homepage"""

    template_name = "index.html"


class RestaurantList(generic.ListView):
    """
    Displays a paginated list of approved restaurants, ordered by creation
    date.
    """

    model = Restaurant
    queryset = Restaurant.objects.filter(status=1).order_by("-created_on")
    template_name = "browse_restaurants.html"
    paginate_by = 8


def restaurant_detail(request, slug):
    """
    Displays detailed view of a specific restaurant, along with its comments.
    Handles new comment submissions.
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


@login_required
def comment_edit(request, slug, comment_id):

    """
    Allows a logged-in user to edit their own comment on a restaurant.
    The comment will be marked as unapproved after editing.
    """

    if request.method == "POST":
        queryset = Restaurant.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.restaurant = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("restaurant_detail", args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):

    """
   Allows a logged-in user to delete their own comment.
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


@login_required
def toggle_favourite(request, slug):

    """
    Allows a logged-in user to add or remove a restaurant from their favourites.
    """

    restaurant = get_object_or_404(Restaurant, slug=slug)

    if request.user in restaurant.favourites.all():
        restaurant.favourites.remove(request.user)
    else:
        restaurant.favourites.add(request.user)

    return redirect(request.META.get("HTTP_REFERER", reverse("home")))


@login_required
def favourite_list(request):

    """
    Displays a list of restaurants favourited by the logged-in user.
    """

    favourites = request.user.favourite.all()
    return render(
        request, "favourite_list.html", {"favourites": favourites})


@login_required
def toggle_like(request, slug):

    """
    Allows a logged-in user to like or unlike a restaurant.
    """

    restaurant = get_object_or_404(Restaurant, slug=slug)

    if request.user in restaurant.likes.all():
        restaurant.likes.remove(request.user)
    else:
        restaurant.likes.add(request.user)

    return redirect("restaurant_detail", slug=restaurant.slug)
