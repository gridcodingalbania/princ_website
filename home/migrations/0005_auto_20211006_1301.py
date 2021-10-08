# Generated by Django 3.2.8 on 2021-10-06 11:01

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0004_alter_homepage_apartament_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='carousel_content',
            field=wagtail.core.fields.StreamField([('Carousel', wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock(required=False))]))], null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='description',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hotel_content',
            field=wagtail.core.fields.StreamField([('Hotel', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False))]))], null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='main_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='navbar_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]