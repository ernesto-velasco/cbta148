from django import template
from django.template import Template
from administration.models import *
from blog.models import *

register = template.Library()
@register.simple_tag()
def show_categories():
    categories = Category.objects.all()
    return categories
@register.simple_tag()
def show_pages(category):
    pages = Page.objects.filter(category=category)
    return pages
@register.simple_tag()
def show_basicinfo():
    basicinfo = Basic_info.objects.all()
    return basicinfo
@register.simple_tag()
def show_post_images(sourse, pk):
    if sourse == "post":
        images = PostImage.objects.filter(property_id=pk)
    elif sourse == "page":
        images = PageImage.objects.filter(property_id=pk)
    return images
@register.simple_tag()
def show_post_files(sourse, pk):
    if sourse == "post":
        images = PostFile.objects.filter(property_id=pk)
    elif sourse == "page":
        images = PageFile.objects.filter(property_id=pk)
    return images