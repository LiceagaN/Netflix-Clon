from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VideoViewSet,
    ViewCreateView,
    FavoriteCreateDestroyView,
    CommentListCreateView,
    UploadURLView
)

router = DefaultRouter()
router.register(r'videos', VideoViewSet, basename='video')

urlpatterns = [
    path('', include(router.urls)),
    path('view/', ViewCreateView.as_view(), name='view-create'),
    path('favorite/', FavoriteCreateDestroyView.as_view(), name='favorite-create-destroy'),
    path('comment/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('upload-url/', UploadURLView.as_view(), name='upload-url')
]   