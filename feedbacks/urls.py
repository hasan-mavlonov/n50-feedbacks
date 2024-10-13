from django.urls import path
from feedbacks.views import (
    homepage, problemspage, offerspage,
    commentspage, unknownpage,
    successpage, register, login, profile, logout_view
)

urlpatterns = [
    path('', homepage, name='home'),
    path('problems/', problemspage, name='problems'),
    path('offers/', offerspage, name='offers'),
    path('comments/', commentspage, name='comments'),
    path('unknown/', unknownpage, name='404'),
    path('register/', register, name='register'),  # Point to the register view
    path('success/', successpage, name='success'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),  # Logout URL
]

