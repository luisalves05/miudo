import uuid

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Url

def init(request):
    return render(request, "tiny/index.html", {})

def make_url(request):
    if request.method == "POST":
        url_site = request.POST['url']
        url_uuid = str(uuid.uuid4())[0:8]
        try:
            url = Url.objects.get(url_uuid = url_uuid)
        except Url.DoesNotExist:
            url = Url.objects.create(url_uuid = url_uuid, url_site = url_site)
            url.save()
    return HttpResponseRedirect("/")
