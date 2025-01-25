from django.contrib import admin
from django.urls import path, include  # Импортируем path и include

# Дополнительный маршрут для главной страницы (если необходимо)
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Добро пожаловать в мой проект Django!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movie.urls')),  # Подключаем маршруты приложения movie
    path('articles/', include('blog.urls')),  # Подключаем маршруты приложения blog
    path('', home, name='home'),  # Маршрут для корневого URL
]
