from .serializers import TranscriptModel,TranscriptSerializer,StudentDetail,StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes,authentication_classes
from rest_framework import permissions,authentication


class GetTranscript(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self,request):
        transcript = TranscriptModel.objects.filter(user=request.user)
        data = TranscriptSerializer(transcript,many=True)
        return Response(data.data)

class GetStudent(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    def get(self,request):
        student = StudentDetail.objects.filter(user=request.user)
        data = StudentSerializer(student,many=True)
        return Response(data.data)