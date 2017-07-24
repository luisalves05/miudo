from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #url(r'^login/$', views.user_login, name='login'),
    url(r'^login/$', auth_views.login, name="login")
]