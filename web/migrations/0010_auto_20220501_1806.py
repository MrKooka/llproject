# Generated by Django 3.2.9 on 2022-05-01 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20220501_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 1, 18, 6, 46, 610104), verbose_name='Дата добавления слова'),
        ),
        migrations.AlterField(
            model_name='word',
            name='number_responses',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество проверок слова'),
        ),
        migrations.AlterField(
            model_name='word',
            name='reply_date',
            field=models.IntegerField(default=1651417606.610104, verbose_name='Дата и время проверки слова'),
        ),
    ]
