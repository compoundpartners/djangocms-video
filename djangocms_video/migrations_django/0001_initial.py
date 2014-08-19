# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, to='cms.CMSPlugin', auto_created=True, parent_link=True, serialize=False)),
                ('movie', models.FileField(null=True, verbose_name='movie file', upload_to=cms.models.pluginmodel.get_plugin_media_path, help_text='use .flv file or h264 encoded video file', blank=True)),
                ('movie_url', models.CharField(max_length=255, null=True, help_text='vimeo or youtube video url. Example: http://www.youtube.com/watch?v=-iJ7bs4mTUY', blank=True, verbose_name='movie url')),
                ('image', models.ImageField(null=True, verbose_name='image', upload_to=cms.models.pluginmodel.get_plugin_media_path, help_text='preview image file', blank=True)),
                ('width', models.PositiveSmallIntegerField(verbose_name='width')),
                ('height', models.PositiveSmallIntegerField(verbose_name='height')),
                ('auto_play', models.BooleanField(default=False, verbose_name='auto play')),
                ('auto_hide', models.BooleanField(default=False, verbose_name='auto hide')),
                ('fullscreen', models.BooleanField(default=True, verbose_name='fullscreen')),
                ('loop', models.BooleanField(default=False, verbose_name='loop')),
                ('bgcolor', models.CharField(max_length=6, default='000000', help_text='Hexadecimal, eg ff00cc', verbose_name='background color')),
                ('textcolor', models.CharField(max_length=6, default='FFFFFF', help_text='Hexadecimal, eg ff00cc', verbose_name='text color')),
                ('seekbarcolor', models.CharField(max_length=6, default='13ABEC', help_text='Hexadecimal, eg ff00cc', verbose_name='seekbar color')),
                ('seekbarbgcolor', models.CharField(max_length=6, default='333333', help_text='Hexadecimal, eg ff00cc', verbose_name='seekbar bg color')),
                ('loadingbarcolor', models.CharField(max_length=6, default='828282', help_text='Hexadecimal, eg ff00cc', verbose_name='loadingbar color')),
                ('buttonoutcolor', models.CharField(max_length=6, default='333333', help_text='Hexadecimal, eg ff00cc', verbose_name='button out color')),
                ('buttonovercolor', models.CharField(max_length=6, default='000000', help_text='Hexadecimal, eg ff00cc', verbose_name='button over color')),
                ('buttonhighlightcolor', models.CharField(max_length=6, default='FFFFFF', help_text='Hexadecimal, eg ff00cc', verbose_name='button highlight color')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
