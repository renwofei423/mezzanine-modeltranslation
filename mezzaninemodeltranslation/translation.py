# -*- coding: utf-8 -*-

from django.contrib import admin
from mezzanine.conf import settings
from modeltranslation.translator import translator, TranslationOptions
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

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

    # admin
    from mezzanine.blog.admin import BlogPostAdmin, BlogCategoryAdmin
    class TransBlogPostAdmin(BlogPostAdmin, TranslationAdmin):
        pass
    admin.site.unregister(BlogPost)
    admin.site.register(BlogPost, TransBlogPostAdmin)

    class TransBlogCategoryAdmin(BlogCategoryAdmin, TranslationAdmin):
        pass
    admin.site.unregister(BlogCategory)
    admin.site.register(BlogCategory, TransBlogCategoryAdmin)

if "mezzanine.pages" in settings.INSTALLED_APPS:
    from mezzanine.pages.models import RichTextPage, Link
    class RichTextPageTranslationOptions(TranslationOptions):
        pass
    translator.register(RichTextPage, RichTextPageTranslationOptions)

    class LinkTranslationOptions(TranslationOptions):
        pass
    translator.register(Link, LinkTranslationOptions)

    # admin
    from mezzanine.pages.admin import PageAdmin, LinkAdmin
    class TransPageAdmin(PageAdmin, TranslationAdmin):
        pass
    admin.site.unregister(RichTextPage)
    admin.site.register(RichTextPage, TransPageAdmin)
    admin.site.unregister(Page)
    admin.site.register(Page, TransPageAdmin)

    class TransLinkAdmin(LinkAdmin, TranslationAdmin):
        pass
    admin.site.unregister(Link)
    admin.site.register(Link, TransLinkAdmin)

if "mezzanine.galleries" in settings.INSTALLED_APPS:
    from mezzanine.galleries.models import Gallery, GalleryImage

    class GalleryImageTranslationOptions(TranslationOptions):
        fields = ('description',)
    translator.register(GalleryImage, GalleryImageTranslationOptions)

    class GalleryTranslationOptions(TranslationOptions):
        pass
    translator.register(Gallery, GalleryTranslationOptions)

    # admin
    from mezzanine.galleries.admin import GalleryAdmin, GalleryImageInline
    class TransGalleryImageInline(GalleryImageInline, TranslationTabularInline):
        pass
    class TransGalleryAdmin(GalleryAdmin, TranslationAdmin):
        inlines = [TransGalleryImageInline,]
        pass
    admin.site.unregister(Gallery)
    admin.site.register(Gallery, TransGalleryAdmin)
