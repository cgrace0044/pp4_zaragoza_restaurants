from django.contrib import admin
from .models import About, Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('about_zaragoza', 'about_me')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'message', 'read',)