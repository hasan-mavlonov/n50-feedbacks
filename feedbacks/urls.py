from django.urls import path
from django.conf.urls.static import static
from feedbacks.views import homepage

urlpatterns = [
    path('', homepage, name='home'),
]

