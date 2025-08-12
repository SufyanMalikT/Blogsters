from django import template
from ..models import ProfilePic
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def pfp(user):
    pic = getattr(user, 'profile_pic', None)
    return pic.img.url if pic else static("blog/img/default-avatar.jpg")