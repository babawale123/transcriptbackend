from django.contrib import admin
from .models import TranscriptModel, StudentDetail

admin.site.register((TranscriptModel,StudentDetail))