# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-01 00:58
from __future__ import unicode_literals

from django.db import migrations
import puput.blocks
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('puput', '0004_auto_20170428_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrypage',
            name='stream_body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('heading', wagtail.wagtailcore.blocks.TextBlock()), ('quote', puput.blocks.QuoteBlock(label='Quote')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False))))), ('table', wagtail.contrib.table_block.blocks.TableBlock(classname='table')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock(label='Raw HTML')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('http', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')])), ('code', wagtail.wagtailcore.blocks.TextBlock())), label='Code')), ('markdown', wagtail.wagtailcore.blocks.StructBlock((('markdown', wagtail.wagtailcore.blocks.TextBlock()),), label='Markdown'))), blank=True, null=True),
        ),
    ]
