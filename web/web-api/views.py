from tkinter import W
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from rest_framework import generics
from rest_framework import status
from ..utils.uploading import upload_functions
from .serializers import WordSerializer
from ..models import Word


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
        print(serializer.error_messages)
        print(serializer.errors)
        print(serializer.default_error_messages)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExistWordView(APIView):

    def get(self, request, *args, **kwargs):
        word = kwargs.get('w', None)
        print(word)
        if word:
            query = Word.objects.filter(eng__contains=word)
            print(query)
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

    





    
        
    


        

# class GetProtocol(APIView):
#     def get(self, request, format=None):
#         regNum = request.query_params.get('regNum', None)
#         if regNum:
#             query = (Oosintegrationpacket.objects
#                      .using('sectionks')
#                      .filter(
#                          regnumber=regNum,
                         
#                          packetstatusid=5,
#                          confirmationresult=1)
#                      .select_related('typeid')
#                      .all())

#             return Response(IntegrationPacketSerializer(query, many=True).data)
#         return Response({'text':'regNum not found'})

#     @classmethod
#     def get_extra_actions(some):
#         return []
