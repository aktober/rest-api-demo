# Generated by Django 2.2 on 2019-04-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190425_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='total_liked',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='unliked',
            field=models.IntegerField(default=0),
        ),
    ]
