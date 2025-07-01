from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Stores information about the site.
    About me and about Letters from Zargoza.
    """

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    about_zaragoza = models.TextField()
    about_me = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    Stores contact messages from users,
    and controls whether a message has been read.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"
