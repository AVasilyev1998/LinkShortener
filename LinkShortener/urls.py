from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def main_redirect(request):
    return redirect('shortener:index')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shortener/', include('shortener.urls'), name='shortener'),
    path('', main_redirect),
]


