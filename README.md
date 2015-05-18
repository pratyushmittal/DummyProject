# `TemplateDoesNotExist` not raised

It seems that `TemplateDoesNotExist` error is
never raised in Django 1.8 tests.

## How to reproduce:

Running `$python manage.py test` should pass the
tests, while `python manage.py runserver` and
opening `127.0.0.1:8000` should raise a
`TemplateDoesNotExist` error.
