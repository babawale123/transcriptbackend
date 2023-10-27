from django.db import models
from account.models import User

class TranscriptModel(models.Model):
    courseTitle = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    score = models.IntegerField()
    grade = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

class StudentDetail(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    matric_no = models.CharField(max_length=255)
    level = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.user.name    