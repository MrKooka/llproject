from statistics import mode
from uuid import uuid4
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, UserManager
from django.contrib.contenttypes.fields import GenericForeignKey
from datetime import datetime
from django.db.models.signals import pre_save,post_save
from .utils.uploading import upload_functions
from .utils.genVoices import genvoice

class Word(models.Model):
    ru = models.CharField(max_length=255, verbose_name='Русское слово')
    eng = models.CharField(max_length=255, verbose_name='Английское слово')
    context = models.CharField(max_length=3000, default='', verbose_name='Контекст слова')
    date = models.DateTimeField(default=datetime.now(), verbose_name='Дата добавления слова')
    reply_date = models.IntegerField(default=datetime.now().timestamp(), verbose_name='Дата и время проверки слова')
    customer = models.ManyToManyField('Customer', related_name='customer', verbose_name='Пользователь')
    is_remember = models.BooleanField(default=False, verbose_name='Выучил ли человек слово или нет')
    number_responses = models.PositiveIntegerField(default=0, verbose_name='Количество проверок слова')
    front_path = models.FileField(null=True,blank=True,verbose_name='Путь до файла для фронта')
    bot_path = models.CharField(max_length=255, verbose_name='Пусть до файла для бота', null=True, blank=True)

    
    
    
    def __str__(self):
        return f'{self.ru}: {self.eng}'


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    chat_id = models.PositiveBigIntegerField(unique=True, null=True, verbose_name='chat_id пользователя в tg', )
    name = models.CharField(max_length=255,verbose_name='Имя пользователя')
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
    def __str__(self):
        return  f'#{self.chat_id} | {self.name}'



class Message(models.Model):
    profile = models.ForeignKey(
        to='Customer',
        verbose_name='Профиль',
        on_delete=models.PROTECT
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    create_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now=True
    )
    
    def __str__(self):
        return f'Сообщение {self.pk} от {self.profile}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'



# class Context(models.Model):
#     ru = models.CharField(max_length=700, verbose_name='Русский перевод')
#     eng = models.CharField(max_length=500, verbose_name='Английский перевод')


# class Voice(models.Model):
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveBigIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#     file = models.FileField()



    

# class Profile(models.Model):
#     external_id = models.PositiveBigIntegerField(
#         verbose_name='ID пользователя в соц сети'
#     )
#     name = models.TextField(
#         verbose_name='Имя пользователя'
#     )
#     def __str__(self):
#         return  f'#{self.external_id} {self.name}'

#     class Meta:
#         verbose_name = 'Профиль'
#         verbose_name_plural = 'Пользователи profile'
# post_save.connect(add_voice, sender=Word)