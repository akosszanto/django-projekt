# Generated by Django 3.1.8 on 2022-12-28 13:34

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20221228_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=0),
            preserve_default=False,
        ),
    ]
