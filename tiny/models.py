from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Url(models.Model):
    url_uuid = models.CharField(primary_key = True, max_length=8)
    url_site = models.TextField()
    
