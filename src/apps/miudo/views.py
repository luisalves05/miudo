import uuid

from random import randint

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Url

def index(request):
    if request.session.has_key("has_url"):
        url = request.session.get("has_url")
        del request.session['has_url']
        return render(request, "miudo/index.html", locals())
    return render(request, "miudo/index.html", {})

def make_url(request):
    if request.method == "POST":

        url = None # initial url
        url_site = request.POST['url']
        url_id = generate_key()

        try:
            url = Url.objects.get(url_id = url_id)
            while url:
                url_id = generate_key()
                url = Url.objects.get(url_id = url_id)
            create_url(request, url_id, url_site)
            request.session["has_url"] = url_id

        except Url.DoesNotExist:
            create_url(request, url_id, url_site)
            request.session["has_url"] = url_id

    return HttpResponseRedirect("/")

def create_url(custom_request, url_id, url_site):
    if custom_request.user.is_authenticated():
        url = Url.objects.create(url_id = url_id, url_site = url_site,
                                url_author = custom_request.user)
    else:
        url = Url.objects.create(url_id = url_id, url_site = url_site)
    url.save()

def generate_key():
    to_choose = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    url_id = ""
    while len(url_id) != 6:
        i = randint(0, len(to_choose) - 1)
        url_id += to_choose[i]
    return url_id

def redirect_url(request, url_id=None):
    try:
        url = Url.objects.get(url_id = url_id)
        url.url_clicked = url.url_clicked + 1
        url.save()
    except Url.DoesNotExist:
        return render(request, "base/page_not_found.html", {})
    return HttpResponseRedirect(url.url_site)
