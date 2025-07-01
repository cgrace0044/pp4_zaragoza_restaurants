from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a restaurant
    """
    class Meta:
        model = Comment
        fields = ("body",)
