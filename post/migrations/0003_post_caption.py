# Generated by Django 4.0.3 on 2022-04-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.TextField(default='SOME STRING', max_length=1500, verbose_name='Caption'),
        ),
    ]
