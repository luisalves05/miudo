from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.init, name = "init"),
    url(r'^make_url/$', views.make_url, name = "make_url"),
    url(r'^(?P<url_id>\w+)/$', views.redirect_url, name="redirect_url")
]
