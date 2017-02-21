from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    #  ^ ForeignKey linkuje ka drugom Modelu (auth.User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #     ovaj metod koristim kasnije u views.py da publishujem draft u okviru post_publish metoda

    def __str__(self):
        return self.title
        # object.__str__(self)¶
        # Called by str(object) and the built-in functions format() and print() to compute the “informal”
        # or nicely printable string representation of an object. The return value must be a string object

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


# sad kad je napravljen model, ides u terminal i kazes: python manage.py makemigrations blog ****
# tako se kreira migracija za taj model (te modele) u bazi podataka
# onda, da migriras, kazes: python manage.py migrate blog  ****


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    # The related_name option allows us to have access to comments from within the Post model.
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
