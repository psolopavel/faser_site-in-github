from django import template
from ..models import Category, Product

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.simple_tag()
def get_day():
    return Product.objects.filter(draft=False).values("data")[:5]