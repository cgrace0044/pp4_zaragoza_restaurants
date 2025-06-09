from django.shortcuts import render
from .models import About
from .forms import ContactForm


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )

def contact_us(request):
    """
    Renders the Contact Form page
    """
    contact_form = ContactForm()

    return render(
        request,
        "about/contact.html",
        {"contact_form": contact_form},
    )