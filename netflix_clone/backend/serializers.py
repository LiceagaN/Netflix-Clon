from rest_framework import serializers
from .models import Movie, Category, Profile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'