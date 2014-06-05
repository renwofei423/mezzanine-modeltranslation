# -*- coding: utf-8 -*-

from mezzanine.conf import settings
from modeltranslation.translator import translator, TranslationOptions

from mezzanine.core.models import RichText, MetaData, Slugged
from mezzanine.pages.models import Page


# Common(shared/base classes)
class MetaDataTranslationOptions(TranslationOptions):
    fields = ("_meta_title", "description", )
translator.register(MetaData, MetaDataTranslationOptions)

class SluggedTranslationOptions(TranslationOptions):
    fields = ("title",)
translator.register(Slugged, SluggedTranslationOptions)

class PageTranslationOptions(TranslationOptions):
    fields = ("title",)
translator.register(Page, PageTranslationOptions)

class RichTextTranslationOptions(TranslationOptions):
    fields = ("content",)
translator.register(RichText, RichTextTranslationOptions)

if "mezzanine.blog" in settings.INSTALLED_APPS:
    from mezzanine.blog.models import BlogPost, BlogCategory
    class BlogPostTranslationOptions(TranslationOptions):
        pass
    translator.register(BlogPost, BlogPostTranslationOptions)

    class BlogCategoryTranslationOptions(TranslationOptions):
        pass
    translator.register(BlogCategory, BlogCategoryTranslationOptions)

if "mezzanine.pages" in settings.INSTALLED_APPS:
    from mezzanine.pages.models import RichTextPage, Link
    class RichTextPageTranslationOptions(TranslationOptions):
        pass
    translator.register(RichTextPage, RichTextPageTranslationOptions)

    class LinkTranslationOptions(TranslationOptions):
        pass
    translator.register(Link, LinkTranslationOptions)

if "mezzanine.galleries" in settings.INSTALLED_APPS:
    from mezzanine.galleries.models import Gallery, GalleryImage

    class GalleryImageTranslationOptions(TranslationOptions):
        fields = ('description',)
    translator.register(GalleryImage, GalleryImageTranslationOptions)

    class GalleryTranslationOptions(TranslationOptions):
        pass
    translator.register(Gallery, GalleryTranslationOptions)

if "mezzanine.generic" in settings.INSTALLED_APPS:
    from mezzanine.generic.models import Keyword
    class KeywordTranslationOptions(TranslationOptions):
        fields = ("title",)
    translator.register(Keyword, KeywordTranslationOptions)

if "mezzanine.forms" in settings.INSTALLED_APPS:
    from mezzanine.forms.models import Form, Field

    class FieldTranslationOptions(TranslationOptions):
        fields = ('label', 'choices', 'default', 'help_text')
    translator.register(Field, FieldTranslationOptions)

    class FormTranslationOptions(TranslationOptions):
        fields = ("title", "content", "button_text", "response")
    translator.register(Form, FormTranslationOptions)





