
from datetime import datetime
import logging
from logging import LogRecord
from django.conf import settings
from django.db.models.fields import CharField,BigAutoField,PositiveBigIntegerField,FloatField
from typing import Tuple,Generator
from django.apps import apps
from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
import pytz
import time


# from web.models import LogModels

def get_models() -> dict:
    """get_models - выдает dict со всеми моделями, зарегистрированными в admin"""
    models_ = {}
    models : Generator = apps.get_app_config('web').get_models()
    for m in models:
        models_.update({m.__name__:m})
    return models_
    
def format_date(log_data: dict[str:str])->dict:
    """filter_data - Форматирует нужным образом время в объекте  LogRecord"""
    default_time_format = settings.LOGGINT_TIME_FORMAT
    timezone = settings.TIME_ZONE

    log_data_ = log_data.copy()
    date = log_data_['created']

    unix_date = int(date)
    parsed_date = datetime.fromtimestamp(unix_date)

    moscow = pytz.timezone(timezone)
    s : datetime = moscow.localize(parsed_date)
    
    log_data_['created'] = s.strftime(default_time_format)
    return log_data_


class SQLHandler(logging.Handler):
    def __init__(self, filename: str):
        logging.Handler.__init__(self)
    
    def emit(self, record:LogRecord):
        message = self.format(record)
        LogModels = get_models()['LogModels']
        log_fields : Tuple[CharField,BigAutoField,FloatField] = LogModels._meta.get_fields()
        log_data = {}
        for field in log_fields[1:]:
            log_data.update({str(field.attname) : getattr(record,field.attname)})

        log_data.update({'message':message})
        print(log_data)
        log_data_ = format_date(log_data)

        log = LogModels(**log_data_)       
        print("log.created >> ", log.created)
        log.save()
        
        print("message>>> ",message)




# args >> ()
# created >> 1654015461.6548219
# exc_info >> None
# exc_text >> None
# filename >> views.py
# funcName >> get
# getMessage >> <bound method LogRecord.getMessage of <LogRecord: test, 10, D:\alpha\LangLearn\llproject\web\webAPI\views.py, 24, "GetWords.get">>
# levelname >> DEBUG
# levelno >> 10
# lineno >> 24
# module >> views
# msecs >> 654.8218727111816
# msg >> GetWords.get
# name >> test
# pathname >> D:\alpha\LangLearn\llproject\web\webAPI\views.py
# process >> 17180
# processName >> MainProcess
# relativeCreated >> 6284.576416015625
# stack_info >> None
# thread >> 13988
# threadName >> Thread-1 (process_request_thread)
# message >>  2022-05-31 19:44:21,654 - DEBUG - D:\alpha\LangLearn\llproject\web\webAPI\views.py - GetWords.get - 24