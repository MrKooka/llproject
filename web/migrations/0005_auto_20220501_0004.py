# Generated by Django 3.2.9 on 2022-04-30 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20220430_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 1, 0, 4, 41, 28403)),
        ),
        migrations.AlterField(
            model_name='word',
            name='reply_date',
            field=models.IntegerField(default='1651352681.028403'),
        ),
    ]
