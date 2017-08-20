from django.contrib import admin
from .models import Url

# Register your models here.
class UrlAdmin(admin.ModelAdmin):
    list_display = ('url_id', 'url_site', 'url_created', 'url_clicked')

admin.site.register(Url, UrlAdmin)