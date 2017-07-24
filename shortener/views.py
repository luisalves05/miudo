import uuid

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Url

def index(request):
    if request.session.has_key("has_url"):
        url = request.session.get("has_url")
        del request.session['has_url']
        return render(request, "shortener/index.html", locals())
    return render(request, "shortener/index.html", {})

def make_url(request):
    if request.method == "POST":
        url_site = request.POST['url']
        url_id = str(uuid.uuid4())[0:8]
        try:
            url = Url.objects.get(url_id = url_id)
            while url:
                url_id = str(uuid.uuid4())[0:8]
                url = Url.objects.get(url_id = url_id)
        except Url.DoesNotExist:
            url = Url.objects.create(url_id = url_id, url_site = url_site)
            url.save()
            request.session["has_url"] = url.url_id
    return HttpResponseRedirect("/")

def redirect_url(request, url_id=None):
    try:
        url = Url.objects.get(url_id = url_id)
        url.url_clicked = url.url_clicked + 1
        url.save()
    except Url.DoesNotExist:
        return render(request, "base/page_not_found.html", {})
    return HttpResponseRedirect(url.url_site) 
