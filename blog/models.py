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
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
    # object.__str__(self)¶
    # Called by str(object) and the built-in functions format() and print() to compute the “informal”
    # or nicely printable string representation of an object. The return value must be a string object


# sad kad je napravljen model, ides u terminal i kazes: python manage.py makemigrations blog ****
# tako se kreira migracija za taj model u bazi podataka
# onda, da migriras, kazes: python manage.py migrate blog  ****