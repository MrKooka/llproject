from typing import Optional
from web.models import Customer
import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions
from datetime import datetime
class AuthBackend(authentication.BaseAuthentication):
    authentication_header_prefex = 'Token'
    

    def authenticate(self, request, token=None, *args, **kwargs)-> Optional[tuple]:
        """
        The `authenticate` method is called on every request regardless of
        whether the endpoint requires authentication.

        `authenticate` has two possible return values:

        1) `None` - We return `None` if we do not wish to authenticate. Usually
                    this means we know authentication will fail. An example of
                    this is when the request does not include a token in the
                    headers.

        2) `(user, token)` - We return a user/token combination when
                             authentication is successful.

                            If neither case is met, that means there's an error
                            and we do not return anything.
                            We simple raise the `AuthenticationFailed`
                            exception and let Django REST Framework
                            handle the rest.
        """

        auth_header = authentication.get_authorization_header(request).split()
        print('auth_header: ',auth_header)
        if not auth_header:
            print('If not auth_header')
            return None

        if not auth_header or auth_header[0].lower() != b'token':
            print(auth_header[0].lower())
            return None

        if len(auth_header) == 1:
            print('1')
            raise exceptions.AuthenticationFailed('Invalid token header. No credential provided')
        elif len(auth_header) > 2:
            print('2')

            raise exceptions.AuthenticationFailed('Invalid token header. Token string should not contains spases')
        try:
            token = auth_header[1].decode('utf-8')
            print('Token',token)
        except UnicodeError:
            print('3')
            raise exceptions.AuthenticationFailed('Invalid token header. Token string should not contains invalid characters')
        return self.authenticate_credential(token)


    def authenticate_credential(self, token) -> tuple:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
            print('payload: ',payload)
        except jwt.PyJWTError:
            print('4')
            raise exceptions.AuthenticationFailed('Invalid authentication. Could not decod token.')

        token_exp = datetime.fromtimestamp(payload['exp'])
        if token_exp < datetime.utcnow():
            print('5')
            raise exceptions.AuthenticationFailed('Token expired')
        try:
            user = Customer.objects.get(id=payload['user_id'])
        except Customer.DoesNotExist:
            print('6')
            raise exceptions.AuthenticationFailed('No user matching this token was found ')
        return user, None

