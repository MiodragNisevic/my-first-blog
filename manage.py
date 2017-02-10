#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)


# da bi napravio bazu, samo kazes u terminalu: python manage.py migrate, posto je vec u
# settings.py podesena DATABASE

# da bi pokrenuo server: python manage.py runserver

# To keep everything tidy, we will create a separate application inside our project:
#  python manage.py startapp blog
# a onda u first/settings.py moras da dodas ovaj novi app "blog" u INSTALLED_APPS

# za git: 1. git init **** 2. git config --global user.name "MiodragNisevic (to mi je github username)" ***
#                   3. git config --global user.email miodrag.nisevic@gmail.com
#  4. napravi .gitignore file i upisi u njega one fajlove koje sad vidis u njemu
#  5. git add --all, git commit -m "Message"
#  6. na githubu, new repository, create repository, HTTPS, poslednja 2 reda ukucaj u terminal
