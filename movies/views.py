from rest_framework.viewsets import ModelViewSet
from .models import Movie, Favorite, Comment
from .permissions import IsOwnerOrAdmin
from .serializers import MovieSerializer, FavoriteSerializer, CommentSerializer
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .moderation import contains_banned_words
from users.models import User
from typing import cast
from django.http import JsonResponse

def movie_list_view(request):
    movies = Movie.objects.all().values("id", "title", "release_year")
    return JsonResponse(list(movies), safe=False)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

class FavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Comment.objects.filter(movie_id=movie_id)

    def perform_create(self, serializer):
        user = cast(User, self.request.user)
        text = serializer.validated_data['text']

        if user.is_blocked:
            raise ValidationError("Your account is blocked.")

        if contains_banned_words(text):
            user.strike_count += 1

            if user.strike_count >= 3:
                user.is_blocked = True

            user.save()
            raise ValidationError("Your comment contains banned words.")

        serializer.save(user=user, movie_id=self.kwargs['movie_id'])

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrAdmin]