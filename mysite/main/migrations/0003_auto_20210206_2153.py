# Generated by Django 3.1.5 on 2021-02-06 21:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210206_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 6, 21, 53, 47, 173087, tzinfo=utc), verbose_name='date published'),
        ),
    ]
