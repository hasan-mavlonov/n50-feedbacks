from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentRegistrationForm
from django.contrib.auth.hashers import make_password  # For password hashing


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def problemspage(request):
    return render(request, 'problems.html')


def offerspage(request):
    return render(request, 'offer.html')


def commentspage(request):
    return render(request, 'comment.html')


def unknownpage(request):
    return render(request, '404.html')


def loginpage(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

def successpage(request):
    return render(request, 'success.html')


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)  # Don't commit yet
            student.save()  # Save the student model
            messages.success(request, 'Registration successful!')

            # Redirect to the success page after registration
            return redirect('successpage')  # Correctly redirect to the success page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentRegistrationForm()

    return render(request, 'register.html', {'form': form})