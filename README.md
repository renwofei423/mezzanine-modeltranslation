mezzanine-modeltranslation
==========================

Easily add internationalization to Mezzanine CMS via django-modeltranslation.
Translated: Page, Gallery, Link, Image, BlogPost including META fields.
Not translated: Keyword

Installation
------------

pip install https://github.com/Romamo/mezzanine-modeltranslation/tarball/master

Configuration
-------------

Add to settings.py

    INSTALLED_APPS = (
        "mezzaninemodeltranslation",
    )

    LANGUAGES = (
        ('en', _('English')),
        ('ru', _('Russian')),
    )

Create database fields

    ./manage.py sync_translation_fields

To prevent duplicate fields in admin must be supplied this patch to django-modeltranslation

    https://github.com/Romamo/django-modeltranslation/commit/2e68811ad0a92d4c50499783bf9245bec3632e42

Todo
----
1. Translate Keyword
2. Include automatic locale url prefix for frontend
