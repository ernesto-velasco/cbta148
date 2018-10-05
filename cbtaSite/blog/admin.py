from django.contrib import admin
from .models import *
from administration.models import *

# Register your models here.
admin.site.register(Basic_info)
admin.site.register(Category)
admin.site.register(Slider)

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 3
class PostFileInline(admin.TabularInline):
    model = PostFile
    extra = 3

class PostAdmin(admin.ModelAdmin):
    inlines = [ PostImageInline, PostFileInline]

admin.site.register(Post, PostAdmin)

class PageImageInline(admin.TabularInline):
    model = PageImage
    extra = 3
class PageFileInline(admin.TabularInline):
    model = PageFile
    extra = 3

class PageAdmin(admin.ModelAdmin):
    inlines = [ PageImageInline, PageFileInline]

admin.site.register(Page, PageAdmin)