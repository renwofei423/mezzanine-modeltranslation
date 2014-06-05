from django.contrib import admin
from mezzanine.conf import settings

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from mezzanine.pages.models import Page

if "mezzanine.blog" in settings.INSTALLED_APPS:
    from mezzanine.blog.models import BlogPost, BlogCategory
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
    # admin
    from mezzanine.pages.admin import PageAdmin, LinkAdmin
    class TransPageAdmin(PageAdmin, TranslationAdmin):
        pass
    admin.site.unregister(RichTextPage)
    admin.site.register(RichTextPage, TransPageAdmin)
    admin.site.unregister(Page)
    admin.site.register(Page, TransPageAdmin)

if "mezzanine.galleries" in settings.INSTALLED_APPS:
    from mezzanine.galleries.models import Gallery, GalleryImage
    # admin
    from mezzanine.galleries.admin import GalleryAdmin, GalleryImageInline
    class TransGalleryImageInline(GalleryImageInline, TranslationTabularInline):
        pass
    class TransGalleryAdmin(GalleryAdmin, TranslationAdmin):
        inlines = [TransGalleryImageInline,]
        pass
    admin.site.unregister(Gallery)
    admin.site.register(Gallery, TransGalleryAdmin)

if "mezzanine.generic" in settings.INSTALLED_APPS:
    from mezzanine.generic.models import Keyword
    admin.site.register(Keyword)
    
if "mezzanine.forms" in settings.INSTALLED_APPS:
    from mezzanine.forms.models import Form, Field
    # admin
    from mezzanine.forms.admin import FormAdmin, FieldAdmin
    class TransFieldAdmin(FieldAdmin, TranslationTabularInline):
        pass
    class TransFormAdmin(FormAdmin, TranslationAdmin):
        inlines = [TransFieldAdmin,]
        pass
    admin.site.unregister(Form)
    admin.site.register(Form, TransFormAdmin)
