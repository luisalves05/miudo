from django.db import models
from django.core.validators import URLValidator
from django.conf import settings

class Url(models.Model):
    url_id = models.CharField(primary_key = True, max_length = 8)
    url_author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1,
    blank = True, null = True)
    url_site = models.TextField()
    url_created = models.DateTimeField(auto_now_add = True)
    url_clicked = models.IntegerField(default = 0)
