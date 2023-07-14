from django import template


register = template.Library()


@register.filter(name='calc_qty_total')
def calc_qty_total(price, quantity):
    return price * quantity
