from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class ContactPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = []
    max_count = 1
    
    body = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'hr',], null=True, blank=False,)

    menu_order = models.IntegerField(default = 0, help_text = "Setup custom menu order")

    promote_panels = Page.promote_panels + [
       FieldPanel('menu_order'),
   ]

    content_panels = Page.content_panels + [
    FieldPanel('body'),
  ]