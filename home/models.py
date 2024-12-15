from django.db import models
from news.models import NewsPage, NewsIndexPage
from schedule.models import Game, Result
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Sponsor(models.Model):
    
  name = models.CharField(max_length=25, null=True, blank=False,)
  position = models.IntegerField(null=True, blank=False)
  logo = models.ForeignKey(
      "wagtailimages.Image",
      null=True,
      blank=False,
      on_delete=models.SET_NULL,
      related_name="+",
      help_text="Sponsor logo",
  )

  panels = [
      FieldPanel('name'),
      FieldPanel('position'),
      FieldPanel('logo'),
  ]

  def __str__(self):
    return self.name


  class Meta:
    ordering = ["position"]

class HomePage(Page):
  max_count = 1



  def get_context(self, request, *args, **kwargs):
    context = super().get_context(request, *args, **kwargs)
    context['latest_news'] = NewsPage.objects.live().public().order_by('-first_published_at')[:5]
    context['all_games'] =  Game.objects.all()
    context['result'] =  Result.objects.first()
    context['news_url'] = NewsIndexPage.objects.first().get_url()
    # print(Game.objects.all())
    return context