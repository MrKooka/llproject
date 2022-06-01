# Generated by Django 3.2.9 on 2022-05-31 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_auto_20220601_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='logmodels',
            name='message',
            field=models.CharField(max_length=255, null=True, verbose_name='Сообщение после форматора'),
        ),
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 0, 51, 0, 67120), verbose_name='Дата добавления слова'),
        ),
        migrations.AlterField(
            model_name='word',
            name='reply_date',
            field=models.IntegerField(default=1654033860.06712, verbose_name='Дата и время проверки слова'),
        ),
    ]