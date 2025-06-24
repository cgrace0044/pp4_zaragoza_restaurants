from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )


def contact_us(request):
    """
    Renders the Contact Form page
    """
    success_message = None

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            success_message = "Your message was sent successfully."
            contact_form = ContactForm()  # reset form after success
    else:
        initial_data = (
            {"email": request.user.email} if request.user.is_authenticated else {}
        )
        contact_form = ContactForm(initial=initial_data)

    return render(
        request,
        "about/contact.html",
        {
            "contact_form": contact_form,
            "success_message": success_message,
        },
    )
