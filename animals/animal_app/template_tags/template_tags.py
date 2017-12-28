from django.template import Library

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
