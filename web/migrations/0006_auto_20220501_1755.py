# Generated by Django 3.2.9 on 2022-05-01 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20220501_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='is_remembere',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 1, 17, 54, 59, 893366)),
        ),
        migrations.AlterField(
            model_name='word',
            name='reply_date',
            field=models.IntegerField(default=1651416899.893366),
        ),
    ]
