import email
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.http import FileResponse
from rest_framework import parsers
from rest_framework import status
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework import viewsets 
import logging.config
from logging import Logger
from ..utils.uploading import upload_functions
from ..utils.auth.google import check_google_auth
from .serializers import UserSerializer, WordSerializer,GoogleAuthSerializer
from ..models import Word


logging.config.dictConfig(settings.LOGGING)

webLogger : Logger = logging.getLogger('web')


class GetWords(APIView):
    def get(self, request, format=None):
        query = Word.objects.filter().all().order_by('-id')
        return Response(WordSerializer(query,many=True).data)

    def post(self, request, format=None):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            w = Word(
                ru=request.data['ru'],
                eng=request.data['eng'],
                context=request.data['context'],
            )

            filename, bot_path, front_path = upload_functions(w)
            w.front_path = str(front_path)
            w.bot_path = str(bot_path/filename)
            w.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        webLogger.warning(f"{serializer.error_messages}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExistWordView(APIView):

    def get(self, request, *args, **kwargs):
        word = kwargs.get('w', None)
        if word:
            query = Word.objects.filter(eng__contains=word)
            if query:
                return Response(WordSerializer(query,many=True).data)
        return Response({'text':'word not exist'}, status=status.HTTP_200_OK)



class DeleteWordView(generics.DestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        data = Word.objects.filter().all().order_by('-id')
        return Response(WordSerializer(data,many=True).data)

    



class GoogleAuthView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, reqest, *args, **kwargs):
        """Подтверждение авторизации через Google"""
        email = reqest.data['email']
        webLogger.debug(f'User auth email: {email}' )
        google_data = GoogleAuthSerializer(data=reqest.data)
        if google_data.is_valid():
            token = check_google_auth(google_data.data)
            return Response(token)
        else:
            # return Response({'err':"Bad google data"})
            return AuthenticationFailed(code=403, detail='Bad data Google')



class UserView(viewsets.ModelViewSet):
    """Просмотр и редактирование данных пользователя"""
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user
    
    def get_object(self):
        return self.get_queryset()
    


class UpdateWordView(APIView):
    def post(self, reqest, *args, **kwargs):

        id = reqest.data['id']
        new_word = reqest.data['newWord']
        eng = reqest.data.get('eng',None)
        if eng:
            word = Word.objects.get(id=id)
            webLogger.debug(f'Update слова user: {word.customer.email} | старое слово: {word.eng}')
            word.eng = new_word
            word.save()
            query = Word.objects.filter().all().order_by('-id')
            return Response(WordSerializer(query,many=True).data)
        word = Word.objects.get(id=id)
        word.ru = new_word
        word.save()
        query = Word.objects.filter().all().order_by('-id')
        return Response(WordSerializer(query,many=True).data)
        

class VoiceView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk',None)
        if id:
            path = Word.objects.get(id=id).bot_path
            print('path:',path)
            return FileResponse(open(path,'rb'))
        return Response(status=status.HTTP_404_NOT_FOUND)