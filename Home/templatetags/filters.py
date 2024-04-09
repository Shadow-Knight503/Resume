from django import template

register = template.Library()

@register.filter
def mult(val, arg):
    return int(val) * int(arg)
