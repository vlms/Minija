from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.blocks import SnippetChooserBlock

from wagtail.blocks import (
    CharBlock,
    # StreamBlock,
    StructBlock,
    ListBlock
)
from wagtail.images.blocks import ImageBlock


@register_snippet
class ClubMember(models.Model):
    
  first_name = models.CharField(max_length=20, null=True, blank=False,)
  last_name = models.CharField(max_length=20, null=True, blank=False,)
  function = models.CharField(max_length=20, null=True, blank=False,)
  foto = models.ForeignKey(
      "wagtailimages.Image",
      null=True,
      blank=False,
      on_delete=models.SET_NULL,
      related_name="+",
      help_text="Sponsor logo",
  )
  player_number = models.IntegerField(null=True, blank=True,)

  panels = [
      FieldPanel('first_name'),
      FieldPanel('last_name'),
      FieldPanel('function'),
      FieldPanel('foto'),
      FieldPanel('player_number'),
  ]

  def __str__(self):
    return self.first_name + " " + self.last_name

  class Meta:
    ordering = ["last_name"]

# class CaptionedImageBlock(StructBlock):
#     image = ImageBlock(required=False)
#     first_name = CharBlock(required=True)
#     last_name = CharBlock(required=True)
#     function = CharBlock(required=False)

#     class Meta:
#         icon = "image"
#         # template = "base/blocks/captioned_image_block.html"

# class HeadingAndCapImgBlock(StructBlock):
#     heading = CharBlock(required=True)
#     cap_images = ListBlock(CaptionedImageBlock())

class HeadingAndMembersBlock(StructBlock):
    heading = CharBlock(required=True)
    members = ListBlock(SnippetChooserBlock(ClubMember))


class TeamPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = []
    max_count = 1

    body = StreamField([
        ('parts', HeadingAndMembersBlock()),
    ])

    menu_order = models.IntegerField(default = 0, help_text = "Setup custom menu order")

    promote_panels = Page.promote_panels + [
       FieldPanel('menu_order'),
   ]

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
