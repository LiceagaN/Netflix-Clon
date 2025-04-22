from rest_framework import serializers

from .models import User, Video, Tag, View, Favorite, Comment, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Video
        fields = '__all__'

class ViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = View
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    video = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'