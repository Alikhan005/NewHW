from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Добро пожаловать на главную страницу!")

urlpatterns = [
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('movies/', include('movie.urls')),
    path('articles/', include('blog.urls')),
]