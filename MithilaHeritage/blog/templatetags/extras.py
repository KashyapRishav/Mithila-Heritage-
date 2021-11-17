from django import template

register=template.Library()

@register.filter(name='get_val')
def get_val(dict, key):
    return dict.get(key)



@register.filter(name='trunc')
def trunc(str):
    return str[0:300] if len(str) > 300 else str