from django import template
from django.utils.html import conditional_escape, format_html
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def color_up2(obj):
    color = 'red'
    text = [str(s) for s in obj]
    if text[0] == ' ':
        text.remove(' ')
    if text[0] != '-':
        color = 'blue'
    return format_html('<b style="color:%s;">%s</b>' % (color, obj))


@register.filter(needs_autoescape=True)
def rubl(obj, autoescape=True):
    try:
        obj = float(obj) * 72
    except:
        obj = obj
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    return mark_safe('%s') % (esc(obj))


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter(needs_autoescape=True)
def color_up(obj, autoescape=True):
    color = '#FF6347'
    # text = etree.tostring(obj, method='text', encoding='utf-8')
    text = [str(s) for s in obj]
    if text[0] == ' ':
        text.remove(' ')
    if text[0] != '-':
        color = '#48D1CC'
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '<a style="color:%s;">%s</a>' % (esc(color), esc(obj))
    return mark_safe(result)
#           format_html('<b style="color:{};">{}</b>', color, text ,obj.status)
