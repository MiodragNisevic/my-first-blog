"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    # The nice thing here is that this just works. We don't have to deal with handling of the form submission nor with
    #  passwords and securing them. Only more thing is left to do. We should add a setting to mysite/settings.py:
    # LOGIN_REDIRECT_URL = '/'
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls')),
    # Django will now redirect everything that comes into 'http://127.0.0.1:8000/'
    # to blog.urls and look for further instructions there. You need to make urls.py in blog folder. except admin,
    # accounts/login and accounts/logout
]
