from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Url


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})

    if request.method == 'POST' and request.is_ajax():
        link = request.POST['link_input']
        if len(link) > 0:
            obj, created = Url.create(url=link)
            if not created:
                return JsonResponse({'link': link, 'shortened_link': obj.get_short_url()})
            else:
                obj.save()
                return JsonResponse({'link': link, 'shortened_link': obj.get_short_url()})
        else:
            return JsonResponse({'error': 'empty_link'})


def link_redirector(request, short_url):
    if Url.objects.filter(short_url=short_url).exists():
        return redirect(f'{Url.objects.get(short_url=short_url).url}')
    return JsonResponse({'get_url': short_url})
