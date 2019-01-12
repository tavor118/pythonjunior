from django import template
from .. import models


register = template.Library()


@register.simple_tag
def get_submenu():
    """
    Return items for submenu
    """
    submenu = models.MainCategory.objects.all()
    return submenu


@register.simple_tag
def get_tags():
    """
    Return tags for tag bar
    """
    tag_bar = models.Tag.objects.all()
    return tag_bar
