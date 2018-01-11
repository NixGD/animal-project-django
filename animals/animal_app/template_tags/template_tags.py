from django.template import Library
from django.utils.safestring import mark_safe
from math import pi, sin, cos

import logging

logger = logging.getLogger("debugging")

register = Library()

@register.inclusion_tag('animal_app/part_table.html')
def part_table(animal, editing_pk=None):
    parts = animal.part_set.all()
    return {"animal_pk": animal.pk, "parts": parts, "editing_pk": editing_pk}

# From http://vanderwijk.info/blog/adding-css-classes-formfields-in-django-templates/#comment-1193609278

@register.filter(name='add_attributes')
def add_attributes(field, css):
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            t, v = d.split(':')
            attrs[t] = v

    return field.as_widget(attrs=attrs)

@register.filter
def hash(h, key):
    return h.get(key)


@register.filter(name='completeness_icon', is_safe=True)
def completeness_icon(animal):
    part_count = animal.part_set.count()
    if (part_count > 0):
        correct = animal.correct_count
        percent = correct / part_count
        if (percent < .5):
            color = "#FF0000"
        elif (percent < 1):
            color = "#0000FF"
        else:
            color = "#00FF00"
        svg = '''<span class="svg-icon svg-baseline" aria-hidden="true">
        <svg viewBox="-1 -1 2 2" style="transform: rotate(-0.25turn)">
          <path d="{}" fill="{}"></path>
        </svg>
        </span>'''.format(svg_path_data(percent), color)
        return mark_safe(svg)
    else:
        return ""


def svg_coordinates_for_percent(percent):
    x = cos(2 * pi * percent)
    y = sin(2 * pi * percent)
    return x, y


def svg_path_data(percent):
    coords = svg_coordinates_for_percent(percent)
    large_arc = 1 if (percent > .5) else 0
    return "M 0,0  L 1,0 A 1 1 0 {} 1 {} {} L 0 0 ".format(large_arc, coords[0], coords[1])