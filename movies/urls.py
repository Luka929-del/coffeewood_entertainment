from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, FavoriteListCreateView, FavoriteDetailView, CommentListCreateView, CommentDeleteView, \
    movie_list_view

router = DefaultRouter()
router.register("movies", MovieViewSet)
app_name = 'movies'

urlpatterns = router.urls + [
    path('favorites/', FavoriteListCreateView.as_view()),
    path('favorites/<int:pk>/', FavoriteDetailView.as_view()),
    path('movies/<int:movie_id>/comments/', CommentListCreateView.as_view()),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view()),
    path('', movie_list_view, name='list'),
]

