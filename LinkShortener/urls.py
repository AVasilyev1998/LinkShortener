from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def main_redirect(request):
    return redirect('sh:index')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sh/', include('shortener.urls'), name='sh'),
    path('', main_redirect),
]


