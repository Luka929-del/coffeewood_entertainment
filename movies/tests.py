import pytest
from django.urls import reverse
from django.test import Client
from movies.models import Movie

@pytest.mark.django_db
def test_movie_creation():
    movie = Movie.objects.create(
        title="Inception",
        description="A mind-bending thriller",
        release_year=2010
    )
    assert movie.title == "Inception"
    assert movie.release_year == 2010


@pytest.mark.django_db
def test_movie_list_view():
    client = Client()
    url = reverse("movies:list")
    response = client.get(url)
    assert response.status_code == 200


