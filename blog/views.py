from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm, EmployeeForm
from django.core.files import File


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') # minus oznacava desc.
    return render(request, 'blog/post_list.html', {'posts': posts})    #drugi argument je template, trazice ga automatski u templates subfolderu koji treba da napravis, a onda blog subfolder i fajl post_list.html


def post_detail(request, pk):
    # Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# So in our view we have two separate situations to handle:
# first, when we access the page for the first time and we want a blank form,
# and second, when we go back to the view with all form data we just typed.
#  So we need to add a condition (we will use if for that):
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #commit=False means that we don't want to save the Post model yet – we want to add the author first
            #  Most of the time you will use form.save() without commit=False
            post.author = request.user
            post.published_date = timezone.now()
            # autora i published_date moram ovako da ubacim jer oni nisu medju elementima forme koje user upisuje
            post.save()
    #         ako se pitas kako je znao da to snimi bas u Post model, pogledaj file forms.py i u njemu PostForm
            return redirect('post_list')
    else:
        form = PostForm
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            with open('employee.txt', 'w') as f:
                myfile = File(f)
                myfile.write('{first_name} ... {last_name} ... {email} ... {password} ' .format(**form.cleaned_data))
        #  ili:       myfile.write('%s ... %s ... %s ... %s ' % (form.cleaned_data['first_name'],
        #                   form.cleaned_data['last_name'], form.cleaned_data['email'], form.cleaned_data['password']))

        # ili more safely: myfile.write('%s ... %s ... %s ... %s ' % (form.cleaned_data('first_name', ''),
        #                   form.cleaned_data('last_name', ''),
        # form.cleaned_data('email', ''), form.cleaned_data('password', ''))
        # which will return an empty string instead of raising an exception if the field is not present in the form.

        # ili: myfile.write('%(first_name)s ... %(last_name)s ... %(email)s ... %(password)s' % form.cleaned_data)

        return render(request, 'blog/employee_thanks.html')
    else:
        form = EmployeeForm
    return render(request, 'blog/employee.html', {'form': form})
