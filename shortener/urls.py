from django.urls import path, re_path
from .views import index, link_redirector

app_name = 'shortener'

urlpatterns = [
    # path('links/', ApiLinksView.as_view(), name='view'),
    path('', index, name='index'),
    re_path(r'(?P<short_url>\w{0,120})/$', link_redirector, name='redirector'),
]
