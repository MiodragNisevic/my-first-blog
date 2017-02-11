from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # ^$ znaci da string pocne i zavrsi se, znaci samo index ce se matchovati na ovo
]
