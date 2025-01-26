from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, CategoryViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
