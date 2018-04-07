from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from miudo.models import Url


@login_required
def dashboard(request):
    user = request.user
    user_urls = Url.objects.filter(url_author = user)
    return render(request, 'account/dashboard.html', {'section': 'dashborad',
    'user_urls': user_urls})
