from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Restaurant(models.Model):
    PRICE_RANGE_CHOICES = [
        ('€', 'Budget'),
        ('€€', 'Moderate'),
        ('€€€', 'Expensive'),
        ('€€€€', 'Luxury'),
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="restaurant_review"
)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, unique=True)
    price_range = models.CharField(max_length=4, choices=PRICE_RANGE_CHOICES)
    description = models.TextField()
    opening_hours = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)