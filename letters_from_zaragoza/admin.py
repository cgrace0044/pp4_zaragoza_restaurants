from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Restaurant, Comment


@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, field for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = (
        "title", "name", "slug", "status", "created_on", "featured")
    search_fields = ["title", "name"]
    list_filter = ("status", "created_on", "featured")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("description", "opening_hours")


# Register your models here.
admin.site.register(Comment)
