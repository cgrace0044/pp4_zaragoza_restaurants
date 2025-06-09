from . import views
from django.urls import path

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path('browse_restaurants/', views.RestaurantList.as_view(), 
         name="browse_restaurants"),
    path('<slug:slug>/', views.restaurant_detail, name='restaurant_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
