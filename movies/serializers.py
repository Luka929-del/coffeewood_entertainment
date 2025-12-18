from rest_framework import serializers
from .models import Movie
from .models import Favorite
from .models import Comment

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'movie', 'created_at')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'movie', 'user', 'text', 'created_at']
        read_only_fields = ['user', 'created_at', 'movie']
