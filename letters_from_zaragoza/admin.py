from django.contrib import admin
from .models import Restaurant, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):
    """Allows admin to manage restaurants via the admin panel"""

    list_display = ("title", "name", "slug", "status", "created_on")
    search_fields = ["title", "name"]
    list_filter = ("status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("description", "opening_hours")


# Register your models here.
admin.site.register(Comment)
