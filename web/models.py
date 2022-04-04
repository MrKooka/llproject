from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User, UserManager
from datetime import datetime


class Word(models.Model):
    ru = models.CharField(max_length=255)
    eng = models.CharField(max_length=255)
    context = models.CharField(max_length=3000, default='')
    date = models.DateTimeField(default=datetime.now())
    reply_date = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    user = models.ManyToManyField('CastomUser')

    def __str__(self):
        return f'{self.ru}: {self.eng}'


class CastomUser(User):
    external_id = models.PositiveBigIntegerField(
        unique=True,
        verbose_name='ID пользователя в соц сети'
    )
    
    name = models.CharField(max_length=255,verbose_name='Имя пользователя')
    guid = models.UUIDField(
         primary_key = True,
         default = uuid4,
         editable = False
         )
    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Пользователи profile'
        
    def __str__(self):
        return  f'#{self.external_id} {self.name}'



class Message(models.Model):
    profile = models.ForeignKey(
        to='web.CastomUser',
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
