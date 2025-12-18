from django.contrib import admin
from .models import Movie
from .models import Favorite


admin.site.register(Movie)
admin.site.register(Favorite)

