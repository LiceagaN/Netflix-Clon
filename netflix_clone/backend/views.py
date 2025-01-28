from rest_framework import viewsets
from .models import Movie, Category, Profile
from .serializers import MovieSerializer, CategorySerializer, ProfileSerializer
from django.http import JsonResponse
from firebase_admin import auth


def verify_firebase_token(request):
    token = request.headers.get('Authorization', '').split('Bearer ')[-1]
    try:
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        return JsonResponse({'status': 'success', 'uid': uid})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=401)

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer