from django.urls import path
from feedbacks.views import (
    homepage, problemsandofferspage, submit_problem, submit_offer,
    commentspage, unknownpage,
    successpage, register, login, profile, logout_view
)

urlpatterns = [
    path('', homepage, name='home'),
    path('problems&offers/', problemsandofferspage, name='problems&offers'),
    path('comments/', commentspage, name='comments'),
    path('unknown/', unknownpage, name='404'),
    path('register/', register, name='register'),  # Point to the register view
    path('success/', successpage, name='success'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('submit_problem/', submit_problem, name='submit_problem'),
    path('submit_offer/', submit_offer, name='submit_offer'),
    # Logout URL
]

