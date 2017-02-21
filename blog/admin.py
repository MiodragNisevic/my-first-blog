# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Post, Comment

# To add, edit and delete the posts we've just modeled, we will use Django admin.


admin.site.register(Post)
admin.site.register(Comment)
# To make our models visible on the admin page,
# we need to register the model with admin.site.register(Post).


# To log in, you need to create a superuser - a user account that has control over everything on the site.
# Go back to the command line, type **** python manage.py createsuperuser ****
