from django.urls import path
from .views import GetTranscript,GetStudent

urlpatterns = [
    path('transcript/',GetTranscript.as_view()),
    path('student/',GetStudent.as_view()),
]
