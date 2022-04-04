from pprint import pprint as pp
from django.db.models.query_utils import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from .serializers import WordSerializer
from ..models import Word


class GetWords(APIView):
    def get(self, request, format=None):
        offset = request.query_params.get('offset', None)
        if offset:
            query = (Word.objects.filter().all()[int(offset):int(offset)+10])
            return Response(WordSerializer(query,many=True).data)
        query = (Word.objects.filter().all()[:20])
        return Response(WordSerializer(query,many=True).data)

    def post(self, request, format=None):
        print(request.data)
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
    


        

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
