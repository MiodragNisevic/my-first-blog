from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, EmployeeForm, CommentForm
from django.core.files import File
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') # minus oznacava desc. a ovaj filter sluzi da predstavi samo published
    return render(request, 'blog/post_list.html', {'posts': posts})    #drugi argument je template, trazice ga automatski u templates subfolderu koji treba da napravis, a onda blog subfolder i fajl post_list.html


def post_detail(request, pk):
    # Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# So in our view we have two separate situations to handle:
# first, when we access the page for the first time and we want a blank form,
# and second, when we go back to the view with all form data we just typed.
#  So we need to add a condition (we will use if for that):
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #commit=False means that we don't want to save the Post model yet – we want to add the author first
            #  Most of the time you will use form.save() without commit=False
            post.author = request.user
            # post.published_date = timezone.now()  ako ga odkomentujem, odmah se publishuje. ovako ide u drafts
            # autora i published_date moram ovako da ubacim jer oni nisu medju elementima forme koje user upisuje
            post.save()
    #         ako se pitas kako je znao da to snimi bas u Post model, pogledaj file forms.py i u njemu PostForm
            return redirect('post_list')
    else:
        form = PostForm
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now() ako ga odkomentujem, odmah se publishuje. ovako ide u drafts
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date') #filteruje samo drafts
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish() #ovaj .publish() metod je napravljen u okviru Post modela u models.py
    return redirect('post_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # False da bih ostale atribute dodao ispod pre nego sto se commituje
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=CommentForm
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    # ovaj red iznad moram jer cu u sledecem redu obrisati comment, pa ne mogu u redirect da kazem pk=comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


@login_required
def employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            with open('employee.txt', 'a') as f:
                myfile = File(f)
                myfile.write('{first_name} ... {last_name} ... {email} ... {password}... ' .format(**form.cleaned_data))
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
