from django.db import models

# Create your models here.

class User(models.Model):
    firebase_uid = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    @property
    def is_authenticated(self):
        return True  # Requerido por DRF para que pase el check
    
    def __str__(self):
        return self.name or self.firebase_uid

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    url = models.URLField()
    thumbnail = models.URLField(blank=True)
    duration = models.DurationField()
    tags = models.ManyToManyField(Tag, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class View(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    position = models.DurationField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'video')

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'video')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)