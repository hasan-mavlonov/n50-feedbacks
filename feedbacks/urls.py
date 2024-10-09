from django.urls import path

from feedbacks.views import homepage

urlpatterns = [
    path('', homepage, name='home'),
]