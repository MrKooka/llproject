# Generated by Django 3.2.9 on 2022-05-31 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_auto_20220518_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now=True, max_length='255', verbose_name='Время лога')),
                ('exc_info', models.CharField(max_length=300, verbose_name='Текст питоновских ошибок')),
                ('exc_text', models.CharField(max_length=300, verbose_name='Тоже текст питоновских ошибок')),
                ('filename', models.CharField(max_length=255, verbose_name='Имя файла')),
                ('funcName', models.CharField(max_length=255, verbose_name='Имя функции')),
                ('levelname', models.CharField(max_length=255, verbose_name='Уровень дебага')),
                ('levelno', models.CharField(max_length=255, verbose_name='Уровень дебага в цифре')),
                ('lineno', models.PositiveIntegerField(verbose_name='Номер строки')),
                ('module', models.CharField(max_length=255, verbose_name='Имя модуля')),
                ('msecs', models.FloatField(verbose_name='Значение в милисек за которое создался логрекорд')),
                ('msg', models.CharField(max_length=255, verbose_name='Текст дебага')),
                ('name', models.CharField(max_length=255, verbose_name='Название логгера')),
                ('pathname', models.CharField(max_length=255, verbose_name='Путь до файла')),
                ('process', models.IntegerField(verbose_name='Пид процесса')),
                ('processName', models.CharField(max_length=255, verbose_name='Имя процесса')),
            ],
        ),
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 49, 43, 777596), verbose_name='Дата добавления слова'),
        ),
        migrations.AlterField(
            model_name='word',
            name='reply_date',
            field=models.IntegerField(default=1654030183.777596, verbose_name='Дата и время проверки слова'),
        ),
    ]
