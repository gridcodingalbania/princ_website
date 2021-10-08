# Generated by Django 3.2.8 on 2021-10-07 09:00

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_homepage_carousel_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='main_image',
        ),
        migrations.AddField(
            model_name='homepage',
            name='main_carousel',
            field=wagtail.core.fields.StreamField([('Carousel', wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('index', wagtail.core.blocks.CharBlock())]))], null=True),
        ),
    ]
