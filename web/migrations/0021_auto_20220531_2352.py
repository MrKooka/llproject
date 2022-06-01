# Generated by Django 3.2.9 on 2022-05-31 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_auto_20220531_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmodels',
            name='exc_info',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Текст питоновских ошибок'),
        ),
        migrations.AlterField(
            model_name='logmodels',
            name='exc_text',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Тоже текст питоновских ошибок'),
        ),
        migrations.AlterField(
            model_name='logmodels',
            name='msg',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст дебага'),
        ),
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 51, 58, 416081), verbose_name='Дата добавления слова'),
        ),
        migrations.AlterField(
            model_name='word',
            name='reply_date',
            field=models.IntegerField(default=1654030318.416081, verbose_name='Дата и время проверки слова'),
        ),
    ]
