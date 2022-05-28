# Generated by Django 3.2.9 on 2022-05-18 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20220516_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 18, 16, 19, 8, 356357), verbose_name='Дата добавления слова'),
        ),
        migrations.AlterField(
            model_name='word',
            name='reply_date',
            field=models.IntegerField(default=1652879948.356357, verbose_name='Дата и время проверки слова'),
        ),
    ]
