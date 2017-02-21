# -*- coding: utf-8 -*-

from django import forms
from .models import Post, Comment


# The nice thing about Django forms is that we can either define one from scratch
# or create a ModelForm which will save the result of the form to the model.


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

# PostForm, as you probably suspect, is the name of our form. We need to tell Django that this form is a ModelForm
#  (so Django will do some magic for us) – forms.ModelForm is responsible for that.
# Next, we have class Meta, where we tell Django which model should be used to create this form (model = Post)

# Finally, we can say which field(s) should end up in our form. In this scenario we want only title and text to be
# exposed – author should be the person who is currently logged in (you!)
# and created_date should be automatically set when we create a post (i.e. in the code), right?


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
