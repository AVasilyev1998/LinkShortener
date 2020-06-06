from django.urls import path, re_path
from .views import index, link_redirector

app_name = 'sh'

urlpatterns = [
    path('', index, name='index'),
    re_path(r'(?P<short_url>\w{0,230})/$', link_redirector, name='redirector'),
]