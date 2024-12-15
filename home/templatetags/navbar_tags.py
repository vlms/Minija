from django import template
from wagtail.models import Page

register = template.Library()


@register.simple_tag
def getnavbar_pages(p):
  list = Page.objects.live().public().in_menu().filter(depth__gte=2).specific()
  list = sorted(list, key=lambda p: getattr(p, 'menu_order'))

  half = (len(list)+1) // 2
  if p == "1":
    return list[:half]
  else: return list[half:]