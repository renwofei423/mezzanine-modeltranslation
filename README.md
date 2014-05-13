mezzanine-modeltranslation
==========================

Easily add internationalization to Mezzanine CMS via django-modeltranslation.
Translated: Page, Gallery, Link, Image, BlogPost including META fields.
Not translated: Keyword

Installation

* Configuration

INSTALLED_APPS = (
    "mezzaninemodeltranslation",
)

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
)

1. Translate Keyword
2. Include automatic locale url prefix for frontend
