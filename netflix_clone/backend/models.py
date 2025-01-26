from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()
    release_date = models.DateField()
    cover_image = models.URLField()
    video_url = models.URLField()
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name