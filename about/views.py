from django.shortcuts import render
from django.contrib import messages
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
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Contact form has been submitted! I will respond to you as soon as possible.")

    contact_form = ContactForm()

    return render(
        request,
        "about/contact.html",
        {"contact_form": contact_form},
    )