from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, Contact


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    List display in About admin
    """
    summernote_fields = ("about_zaragoza", "about_me")
    list_display = (
        "title",
        "location",
        "email",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "message",
        "read",
    )
