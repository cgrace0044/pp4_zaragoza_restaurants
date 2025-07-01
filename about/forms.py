from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form class for users to contact us
    """
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
