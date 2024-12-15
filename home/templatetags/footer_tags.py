from django import template
from home.models import Sponsor

register = template.Library()

@register.simple_tag
def get_sponsors():
  return Sponsor.objects.all()