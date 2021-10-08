from django.db import models
from wagtail.core.blocks.field_block import RichTextBlock

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

class HomePage(Page):
    template = "home/home_page.html"

    navbar_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    
    main_carousel = StreamField([
     ('Carousel', blocks.StructBlock([
         ('photo', ImageChooserBlock(required=False)),
         ('index',blocks.CharBlock()),
     ]))
    ],null=True,blank=False)

    image2 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    description = RichTextField(blank=False, null=True)
    hotel_content = StreamField([
     ('Hotel', blocks.StructBlock([
         ('title',blocks.CharBlock()),
         ('description', blocks.RichTextBlock()),
         ('photo', ImageChooserBlock(required=False))
     ]))
    ],null=True,blank=False)

    apartament_content = StreamField([
     ('Apartaments', blocks.StructBlock([
         ('title',blocks.CharBlock()),
         ('description', blocks.RichTextBlock()),
         ('price',blocks.CharBlock()),
         ('photo', ImageChooserBlock(required=False))
     ]))
    ],null=True,blank=False)

    carousel_content = StreamField([
     ('Carousel', blocks.StructBlock([
         ('photo', ImageChooserBlock(required=False)),
         ('index',blocks.CharBlock()),
     ]))
    ],null=True,blank=False)

    contact = StreamField([
        ('Contact', blocks.StructBlock([
            ('information',  blocks.RichTextBlock()),
            ('adress',blocks.CharBlock()),
            ('phone',blocks.CharBlock())
        ]))
    ],null=True,blank=False)

    content_panels = Page.content_panels + [
        ImageChooserPanel("navbar_image"),
        StreamFieldPanel("main_carousel"),
        ImageChooserPanel("image2"),
        FieldPanel("description"),
        StreamFieldPanel("hotel_content"),
        StreamFieldPanel("apartament_content"),
        StreamFieldPanel("carousel_content"),
        StreamFieldPanel("contact")
    ]