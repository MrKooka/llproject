# Generated by Django 3.2.9 on 2022-05-01 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20220501_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='is_remembere',
            new_name='is_remember',
        ),
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 1, 17, 55, 25, 869398)),
        ),
        migrations.AlterField(
            model_name='word',
            name='reply_date',
            field=models.IntegerField(default=1651416925.869398),
        ),
    ]
