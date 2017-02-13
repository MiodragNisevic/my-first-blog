from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # ^$ znaci da string pocne i zavrsi se, znaci samo index ce se matchovati na ovo
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # In django, named capturing groups are passed to your view as keyword arguments.
    # Unnamed capturing groups (just a parenthesis) are passed to your view as arguments.
    # The ?P is a named capturing group, as opposed to an unnamed capturing group.

    # (?P<pk>\d+) – this part means Django will take everything that you place here and transfer it
    # to a view as a variable called pk
    # \d also tells us that it can only be a digit, not a letter (so everything between 0 and 9).
    # + means that there needs to be one or more digits there
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^file/$', views.employee, name='employee'),
]
