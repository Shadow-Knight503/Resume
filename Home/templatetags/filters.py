from django import template

register = template.Library()

@register.filter
def mult(val, arg):
    return int(val) * int(arg)

@register.filter
def rem_spc(val):
    return val.replace(' ', '_')
