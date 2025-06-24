from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Save for later"), (1, "Publish now"))


# Create your models here.
class Restaurant(models.Model):
    """Model for Restaurant"""

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="restaurant_review"
    )
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, unique=True)
    low_price_range = models.IntegerField(default=0)
    high_price_range = models.IntegerField(default=10)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField("image", default="placeholder")
    status = models.IntegerField(choices=STATUS, default=0)
    favourites = models.ManyToManyField(
        User, related_name="favourite", default=None, blank=True)
    likes = models.ManyToManyField(
        User, related_name="restaurant_like", blank=True)

    def __str__(self):
        return f"{self.name} | written by {self.author}"

    def number_of_likes(self):
        return self.likes.count()

    @property
    def price_range(self) -> str:
        if self.high_price_range <= 10:
            return "Budget"
        elif self.high_price_range <= 20:
            return "Moderate"
        elif self.high_price_range <= 30:
            return "Expensive"
        else:
            return "Luxury"


class Comment(models.Model):
    """Model for Comment"""

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """To display the comments by created_on in ascending order"""

        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author.username}"
