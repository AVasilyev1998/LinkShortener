from django.db import models
import hashlib


class Url(models.Model):
    url = models.URLField(unique=True)
    short_url = models.URLField(db_index=True)
    created = models.DateTimeField(auto_now=True)

    @classmethod
    def create(cls, url):
        obj = cls.objects.filter(url=url).exists()
        if obj:
            return Url.objects.get(url=url), False
        else:
            url = cls(url=url, short_url=cls.hash_url(url))
        return url, True

    def __str__(self):
        return f'{self.url} | {self.short_url}'

    def get_short_url(self):
        return self.short_url

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    @staticmethod
    def hash_url(input):
        if isinstance(input, str):
            return f'{hashlib.md5(input.encode("utf-8")).hexdigest()[:8]}'
        else:
            raise TypeError('url must be a string!')
