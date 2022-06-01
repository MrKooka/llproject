from web.webAPI import serializers
from rest_framework import status
from django.contrib.auth import get_user_model

from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
import logging.config
from logging import Logger

from web.models import Customer
from django.conf import settings

from .base_auth import create_token
logging.config.dictConfig(settings.LOGGING)

webLogger : Logger = logging.getLogger('web')


def check_google_auth(google_user:serializers.GoogleAuthSerializer) -> dict:
    try:
        email = google_user['email']
        webLogger.debug(f'Проверка токена google_user: {email}')
        id_token.verify_oauth2_token(google_user['token'], requests.Request(), settings.GOOGLE_CLIENT_ID)

    except ValueError:
        webLogger.warning(f'Проверка токена не прошла успешно {google_user}')
        raise AuthenticationFailed(code=403,detail='Bad Google token')
    
    cust, _ =  Customer.objects.get_or_create(email=google_user['email'])
    return create_token(cust.id)

    
