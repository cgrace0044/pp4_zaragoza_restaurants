from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Model for about text
    """
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, unique=True)
    zaragoza_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    about_zaragoza = models.TextField()
    about_me = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    Model for contacting us
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"