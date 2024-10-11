from django.urls import path
from feedbacks.views import homepage, problemspage, offerspage,commentspage, unknownpage, loginpage, register, successpage

urlpatterns = [
    path('', homepage, name='home'),
    path('problems/', problemspage, name='problems'),
    path('offers/', offerspage, name='offers'),
    path('comments/', commentspage, name='comments'),
    path('unknown/', unknownpage, name='404'),
    path('login/', loginpage, name='login'),
    path('register/', register, name='register'),  # Use the actual register view here
    path('success/', successpage, name='success'),

]

