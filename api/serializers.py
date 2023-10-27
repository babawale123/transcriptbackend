from rest_framework import serializers
from .models import TranscriptModel,StudentDetail

class TranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranscriptModel
        fields = ['id','courseTitle','unit','score','grade','user']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields =  ['id','first_name','last_name','matric_no','level']