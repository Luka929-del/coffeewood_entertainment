from rest_framework.viewsets import ModelViewSet
from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsAdminOrReadOnly

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]

