from django.contrib.auth.models import User
from django.db import models


class StudentModel(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class FeedbackModel(models.Model):
    rating = models.IntegerField(default=0)
    comment = models.TextField(default='')
    user = models.ForeignKey(StudentModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'
