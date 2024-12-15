from django.db import models
from wagtail.models import Page
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.fields import StreamField, RichTextField
from wagtail.images.blocks import ImageBlock
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.blocks import SnippetChooserBlock

from wagtail.contrib.routable_page.models import RoutablePageMixin, path

from schedule.models import Result

# class NewsIndexPage(RoutablePageMixin, Page):
#   max_count = 1
#   subpage_types = ["news.NewsPage"]
#   parent_page_types = ['home.HomePage']

#   @path('') 
#   @path('<int:page_num>/') # will override the default Page serving mechanism
#   def old_news(self, request, page_num=1):
#     the_news = NewsPage.objects.live().public().order_by('-first_published_at')[5:]
#     print(self.slug)
#     print(self.get_url())
#     page = page_num
#     paginator = Paginator(the_news, 6)
#     try:
#         the_news = paginator.page(page)
#     except PageNotAnInteger:
#         the_news = paginator.page(1)
#     except EmptyPage:
#         the_news = paginator.page(paginator.num_pages)

    # NOTE: We can use the RoutablePageMixin.render() method to render
    # the page as normal, but with some of the context values overridden
    # return self.render(request, context_overrides={
    #     'news': the_news
    # })

  # @path('<int:page_num>/') # will override the default Page serving mechanism
  # def old_news(self, request, page_num=None):
  #   the_news = NewsPage.objects.live().public().order_by('-first_published_at')[5:]

  #   page = page_num
  #   paginator = Paginator(the_news, 6)
  #   try:
  #       the_news = paginator.page(page)
  #   except PageNotAnInteger:
  #       the_news = paginator.page(1)
  #   except EmptyPage:
  #       the_news = paginator.page(paginator.num_pages)

  #   # NOTE: We can use the RoutablePageMixin.render() method to render
  #   # the page as normal, but with some of the context values overridden
  #   return self.render(request, context_overrides={
  #       'news': the_news
  #   })

class NewsIndexPage(Page):
  subpage_types = ["news.NewsPage"]
  parent_page_types = ['home.HomePage']
  def get_context(self, request):
    context = super().get_context(request)
    the_news = NewsPage.objects.live().public().order_by('-first_published_at')[5:]
    the_slug = self.slug
    page = the_slug[-1:]
    paginator = Paginator(the_news, 6)
    try:
        the_news = paginator.page(page)
    except PageNotAnInteger:
        the_news = paginator.page(1)
    except EmptyPage:
        the_news = paginator.page(paginator.num_pages)
    context['news'] =the_news
    return context

class NewsPage(Page):
  parent_page_types = ['news.NewsIndexPage']
  subpage_types = []
 
  intro = models.TextField(blank=False, max_length=210)
  intro_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="News intro image",
    )
  
  full_description = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'hr', 'embed'])

  media = StreamField([
        ('images', ImageBlock()),
    ], blank=True)
  
  # game_is = models.ForeignKey("schedule.Result",null=True,blank=True,on_delete=models.SET_NULL, related_name='game_description')
  game_is =  models.OneToOneField("schedule.Result", null=True, blank=True, on_delete=models.SET_NULL)

  players = StreamField([
    ('player', SnippetChooserBlock("team.ClubMember", required=False)),
  ], blank=True)

  reserve_players = StreamField([
    ('player', SnippetChooserBlock("team.ClubMember", required=False)),
  ], blank=True)

  content_panels = Page.content_panels + [
    FieldPanel('intro'),
    FieldPanel('intro_image'),
    FieldPanel('full_description'),
    FieldPanel('media'),
    FieldPanel('game_is'),
    FieldPanel('players'),
    FieldPanel('reserve_players')
  ]
  