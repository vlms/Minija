from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.models import Page

@register_snippet
class Team(models.Model):
  
  name = models.CharField(max_length=25)
  logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Team logo",
    )
  
  panels = [
    FieldPanel('name'),
    FieldPanel('logo'),
  ]
  
  def __str__(self):
        return self.name
  
  class Meta:
    ordering = ["name"]

@register_snippet
class Game(models.Model):
    GAME_TYPE_CHOICES = {
       "PIRMA LYGA": "TOP SPORT PIRMA LYGA",
       "DRAUGISKOS": "DRAUGIŠKOS RUNGTYNĖS",
       "LFF TAURE": "LFF TAURĖ"
    }
    home_team = models.ForeignKey("schedule.Team",null=False,blank=False,on_delete=models.CASCADE,related_name='+')
    away_team = models.ForeignKey("schedule.Team",null=False,blank=False,on_delete=models.CASCADE, related_name='+')
    game_date = models.DateTimeField()
    game_type = models.CharField(
        max_length=20,
        choices=GAME_TYPE_CHOICES,
        default="PIRMA LYGA",
    )

    panels = [
    FieldPanel('home_team'),
    FieldPanel('away_team'),
    FieldPanel('game_date'),
    FieldPanel('game_type'),
    ]

    def __str__(self):
        return self.home_team.name + " vs " + self.away_team.name
    
    class Meta:
       ordering = ["game_date"]


@register_snippet
class Result(models.Model):
    the_game =  models.OneToOneField(Game, on_delete=models.CASCADE)

    home_team_score = models.CharField(max_length=2, blank =  False, null = False)
    away_team_score = models.CharField(max_length=2, blank =  False, null = False)


    def __str__(self):
        return str(self.the_game) + "  " + self.home_team_score + ":" + self.away_team_score
    
    class Meta:
        ordering = ["-the_game__game_date"]


class SchedulePage(Page):
  max_count = 1
  subpage_types = []
  parent_page_types = ['home.HomePage']

  menu_order = models.IntegerField(default = 0, help_text = "Setup custom menu order")

  promote_panels = Page.promote_panels + [
      FieldPanel('menu_order'),
  ]

  def get_context(self, request):
    context = super().get_context(request)
    context['games'] = Game.objects.all()
    return context