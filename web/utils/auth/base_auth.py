from datetime import datetime, timedelta
import jwt
from django.conf import settings
import logging.config
from logging import Logger
from rest_framework.exceptions import AuthenticationFailed

logging.config.dictConfig(settings.LOGGING)

webLogger : Logger = logging.getLogger('web')


def create_token(user_id: int) -> dict:
    """Создание токена"""
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    webLogger.debug(f'Создание токена access_token_expires: {access_token_expires}')
    return {
        "user_id": user_id,
        "access_token": create_access_token(data={"user_id":user_id}, expires_delta=access_token_expires),
        "token_type": "Token"
    }

def create_access_token(data:dict, expires_delta: timedelta = None)-> dict:
    """Создание access токена"""
    to_encode = data.copy()
    if expires_delta is not None:
        expire = datetime.utcnow() + expires_delta
        webLogger.debug(f'Создание expire для токена expires_delta: {expires_delta} | expire: {expire}')
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
        webLogger.debug(f'Создание expire для токена expires_delta: {expires_delta} | expire: {expire}')

    to_encode.update({'exp':expire, 'sub':"access"}) 
    try:
        encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encode_jwt
    except Exception:
        webLogger.error('Попытка енкода токена', exc_info=True)
        AuthenticationFailed(code=403,detail='Cant encode token')
