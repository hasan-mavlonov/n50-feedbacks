from django.db import models
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.utils.translation import gettext_lazy as _


class StudentModel(models.Model):
    first_name = models.CharField(max_length=100, null=True, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, null=True, verbose_name=_('Last Name'))
    username = models.CharField(max_length=50, unique=True, verbose_name=_('Username'))
    email = models.EmailField(max_length=100, unique=True, verbose_name=_('Email'))
    password = models.CharField(max_length=128, verbose_name=_('Password'))  # Handle this securely
    organization_name = models.CharField(max_length=100, null=True, verbose_name=_('Organization Name'))
    location = models.CharField(max_length=100, null=True, verbose_name=_('Location'))
    linkedin_profile = models.URLField(max_length=200, null=True, blank=True, verbose_name=_('LinkedIn Profile Link'))
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True,
                                        verbose_name=_('Profile Picture'))
    @property
    def full_name(self):
        # Combine first and last names for full name
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')


class FeedbackModel(models.Model):
    rating = models.IntegerField(default=0)
    comment = models.TextField(default='')
    user = models.ForeignKey(StudentModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')


