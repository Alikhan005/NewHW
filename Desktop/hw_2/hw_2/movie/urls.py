from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_movies, name='get_movies'),  # Для вывода всех фильмов
    path('<int:id>/', views.get_movie_by_id, name='get_movie_by_id'),  # Для вывода фильма по ID
]
