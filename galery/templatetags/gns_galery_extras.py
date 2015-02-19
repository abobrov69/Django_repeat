from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='strip')
@stringfilter
def templ_strip(value):
    return value.strip()