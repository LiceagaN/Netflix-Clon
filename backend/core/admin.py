from django.contrib import admin
from .models import User, Video, Tag, View, Favorite, Comment, Category
# Register your models here.
admin.site.register(User)
admin.site.register(Video)
admin.site.register(Tag)
admin.site.register(View)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(Category)

