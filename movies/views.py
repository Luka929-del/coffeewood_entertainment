from rest_framework.viewsets import ModelViewSet
from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework import generics, permissions
from .models import Favorite
from .serializers import FavoriteSerializer

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]

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