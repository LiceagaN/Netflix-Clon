from rest_framework.views import APIView
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Video, Favorite, View, Comment
from .serializers import (
    VideoSerializer, ViewSerializer, FavoriteSerializer, CommentSerializer
)
from core.utils.authentication import FirebaseAuthentication
from core.utils.s3 import generate_presigned_url

class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]

class ViewCreateView(APIView):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = ViewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class FavoriteCreateDestroyView(APIView):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]

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

class CommentListCreateView(APIView):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]

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

class UploadURLView(APIView):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file_name = request.data.get('file_name')
        if not file_name:
            return Response({'error': 'file_name is required'}, status=status.HTTP_400_BAD_REQUEST)

        url = generate_presigned_url(file_name)
        if not url:
            return Response({'error': 'Failed to generate URL'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'upload_url': url}, status=status.HTTP_200_OK)
