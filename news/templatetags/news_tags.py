from django import template
from news.models import NewsIndexPage

register = template.Library()

@register.simple_tag
def get_news_page(num=1):
  slug = "news" + str(num)
  return NewsIndexPage.objects.get(slug=slug)