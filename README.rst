PythonJunior
============


.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Ready-to-use site for organising web-links.
Links can have main category, subcategory and tags.


Inittilization
--------------

Strongly recommended to use venv for creating virtual environment.


Install needed packages for development::

    $ pip install -r requirements/local.txt


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

