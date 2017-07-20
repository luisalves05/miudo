from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Url(models.Model):
    url_id = models.AutoField(primary_key = True)
    url_site = models.TextField(validators = [URLValidator()])
