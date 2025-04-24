from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from .models import User, Video, Tag, View, Favorite, Comment, Category
from core.utils.authentication import AuthenticatedAPIView
from rest_framework import generics
from rest_framework.response import Response
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

class ViewCreateView(AuthenticatedAPIView):
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = ViewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)  

class FavoriteCreateDestroyView(AuthenticatedAPIView):
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = FavoriteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request):
        video_id = request.query_params.get('video')
        favorite = Favorite.objects.filter(user=request.user, video_id=video_id).first()
        if favorite:
            favorite.delete()
            return Response({'mensaje': 'Favorito eliminado'}, status=204)
        return Response({'mensaje': 'Favorito no encontrado'}, status=404)

class CommentListCreateView(AuthenticatedAPIView):
    def get(self, request):
        video_id = request.query_params.get('video')
        comments = Comment.objects.filter(video_id=video_id) if video_id else Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
