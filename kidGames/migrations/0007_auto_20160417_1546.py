# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-17 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import kidGames.models


class Migration(migrations.Migration):

    dependencies = [
        ('kidGames', '0006_auto_20160417_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to=kidGames.models.UploadToPathAndRename('media/upload/here')),
        ),
        migrations.AlterField(
            model_name='question',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to=kidGames.models.UploadToPathAndRename('media/upload/here')),
        ),
        migrations.AlterField(
            model_name='question',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to=kidGames.models.UploadToPathAndRename('media/upload/here')),
        ),
        migrations.AlterField(
            model_name='question',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to=kidGames.models.UploadToPathAndRename('media/upload/here')),
        ),
        migrations.AlterField(
            model_name='question',
            name='img5',
            field=models.ImageField(blank=True, null=True, upload_to=kidGames.models.UploadToPathAndRename('media/upload/here')),
        ),
        migrations.AlterField(
            model_name='question',
            name='img6',
            field=models.ImageField(blank=True, null=True, upload_to=kidGames.models.UploadToPathAndRename('media/upload/here')),
        ),
        migrations.AlterField(
            model_name='question',
            name='img7',
            field=models.ImageField(blank=True, null=True, upload_to=kidGames.models.UploadToPathAndRename('media/upload/here')),
        ),
        migrations.AlterField(
            model_name='question',
            name='img8',
            field=models.ImageField(blank=True, null=True, upload_to=kidGames.models.UploadToPathAndRename('media/upload/here')),
        ),
        migrations.AlterField(
            model_name='question',
            name='img9',
            field=models.ImageField(blank=True, null=True, upload_to=kidGames.models.UploadToPathAndRename('media/upload/here')),
        ),
    ]
