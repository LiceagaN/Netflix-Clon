from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from .models import User, Video, Tag, View, Favorite, Comment, Category
from .serializers import (
    VideoSerializer,
    TagSerializer,
    ViewSerializer,
    FavoriteSerializer,
    CommentSerializer,
    CategorySerializer
)
# Create your views here.
class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

class ViewCreateView(generics.CreateAPIView):
    serializer_class = ViewSerializer

class FavoriteCreateDestroyView(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        video_id = self.request.query_params.get('video_id')
        return Comment.objects.filter(video_id=video_id) if video_id else Comment.objects.all()