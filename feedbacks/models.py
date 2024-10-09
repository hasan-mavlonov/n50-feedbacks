from django.db import models
from django.utils.translation import gettext_lazy as _


class StudentModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_('Full name'))
    username = models.CharField(max_length=10, verbose_name=_('Username'))
    email = models.EmailField(max_length=100, verbose_name=_('Email'))
    password = models.CharField(max_length=100, verbose_name=_('Password'))  # Handle this securely

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')  # Fix the plural verbose name


class FeedbackModel(models.Model):
    rating = models.IntegerField(default=0)
    comment = models.TextField(default='')
    user = models.ForeignKey(StudentModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')  # Singular is OK here, but plural can be 'Feedbacks'
