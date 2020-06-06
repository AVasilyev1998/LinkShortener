from django.shortcuts import render, redirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from urllib.parse import urlparse

from .models import Url
import logging
import datetime

logger = logging.getLogger(__name__)


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})

    if request.method == 'POST' and request.is_ajax():
        logger.info(f'{datetime.datetime.now().strftime("%D|%T")} got request with {request.POST}')
        request_link = request.POST['link_input']

        def is_link_valid(link: str) -> bool:
            validator = URLValidator()
            try:
                validator(link)
            except ValidationError:
                return False
            return True

        is_link_valid(request_link)
        # checking if link is valid
        if is_link_valid(request_link):
            def is_link_absolute(link):
                return bool(urlparse(link).netloc)

            if not is_link_absolute(request_link):
                logger.error(f'{datetime.datetime.now().strftime("%D|%T")} link isn`t absolute {request_link}')
                return JsonResponse({'error': 'is not full. Please specify the full link.'})

            # using reloaded method create in Url model
            obj, created = Url.create(url=request_link)
            if not created:
                return JsonResponse({'link': request_link, 'shortened_link': obj.get_short_url()})
            else:
                obj.save()
                return JsonResponse({'link': request_link, 'shortened_link': obj.get_short_url()})
        else:
            logger.error(f'{datetime.datetime.now().strftime("%D|%T")} link invalid {request_link}')
            return JsonResponse({'error': 'is invalid'})

    else:
        logger.warning(f'got request that is not supposed to be')


def link_redirector(request, short_url):
    if Url.objects.filter(short_url=short_url).exists():
        return redirect(f'{Url.objects.get(short_url=short_url).url}')
    return JsonResponse({'get_url': short_url})
