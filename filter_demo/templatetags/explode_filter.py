from django import template
from django.template.defaultfilters import stringfilter
register=template.Library()


@register.filter

def explode(value,separator):
    return value.split(separator)

#@register.filter
#@stringfilter
#def generic_string_filter(value,arg):
