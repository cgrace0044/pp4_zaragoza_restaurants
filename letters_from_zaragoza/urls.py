from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "browse_restaurants/", views.RestaurantList.as_view(),
        name="browse_restaurants"
    ),
    path(
        "favourite/<slug:slug>/", views.toggle_favourite,
        name="toggle_favourite"),
    path("favourites/", views.favourite_list, name="favourites"),
    path("like/<slug:slug>/", views.toggle_like, name="toggle_like"),
    path("<slug:slug>/", views.restaurant_detail, name="restaurant_detail"),
    path("restaurant/<slug:slug>/comment/",
         views.add_comment,
         name="add_comment"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
]
