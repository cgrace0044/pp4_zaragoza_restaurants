from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

from about.models import About
from .models import Restaurant, Comment
from .forms import CommentForm


def home(request):
    about = About.objects.all().order_by("-updated_on").first()
    featured_restaurants = Restaurant.objects.filter(
        featured=True, status=1)[:6]

    return render(request, "index.html", {
        "about": about,
        "featured_restaurants": featured_restaurants
    })


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
    """
    restaurant = get_object_or_404(Restaurant, slug=slug, status=1)
    comments = restaurant.comments.all().order_by("-created_on")
    comment_count = restaurant.comments.filter(approved=True).count()
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


def add_comment(request, slug):
    """
    Handles new comment submission for a specific restaurant.
    """
    restaurant = get_object_or_404(Restaurant, slug=slug, status=1)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.restaurant = restaurant
            comment.save()
            messages.success(request, "Comment submitted and awaiting approval")
        else:
            messages.error(request, "There was an error with your comment.")

    return redirect("restaurant_detail", slug=slug)


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
            messages.add_message(
                request, messages.ERROR, "Error updating comment!")

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
    Allows a logged-in user to add or remove a restaurant
    from their favourites.
    """

    restaurant = get_object_or_404(Restaurant, slug=slug)

    if request.user in restaurant.favourites.all():
        restaurant.favourites.remove(request.user)
        messages.info(
            request,
            f"You have removed '{restaurant.name}' from your favourites."
        )
    else:
        restaurant.favourites.add(request.user)
        messages.success(
            request, f"You have added '{restaurant.name}' to your favourites."
        )

    return redirect(request.META.get("HTTP_REFERER", reverse("home")))


@login_required
def favourite_list(request):
    """
    Displays a list of restaurants favourited by the logged-in user.
    """

    favourites = request.user.favourite.all()
    return render(request, "favourite_list.html", {"favourites": favourites})


@login_required
def toggle_like(request, slug):
    """
    Allows a logged-in user to like or unlike a restaurant.
    """

    restaurant = get_object_or_404(Restaurant, slug=slug)

    if request.user in restaurant.likes.all():
        restaurant.likes.remove(request.user)
        messages.info(request, f"You have unliked {restaurant.name}.")
    else:
        restaurant.likes.add(request.user)
        messages.success(request, f"You have liked {restaurant.name}.")

    return redirect("restaurant_detail", slug=restaurant.slug)
