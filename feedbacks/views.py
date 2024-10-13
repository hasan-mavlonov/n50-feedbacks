from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import StudentModel
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentRegistrationForm, StudentProfileForm
from django.contrib.auth.hashers import make_password


def homepage(request):
    return render(request, 'index.html')


def problemspage(request):
    return render(request, 'offer.html')


def offerspage(request):
    return render(request, 'problems.html')


def commentspage(request):
    return render(request, 'comment.html')


def unknownpage(request):
    return render(request, '404.html')


def loginpage(request):
    return render(request, 'login.html')


def registerpage(request):
    return render(request, 'register.html')


def successpage(request):
    return render(request, 'success.html')


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            # Get the student instance from the form
            student = form.save(commit=False)  # Don't commit yet

            # Hash the password before saving
            student.password = make_password(form.cleaned_data['password1'])
            student.save()  # Save the student model

            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to a success page or another view
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentRegistrationForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists
        try:
            user = StudentModel.objects.get(username=username)
        except StudentModel.DoesNotExist:
            user = None

        # Verify the password
        if user and check_password(password, user.password):
            # Set session variable
            request.session['user_id'] = user.id  # Save user id in session
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to homepage or success page
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')  # Render the login pagee




def logout_view(request):
    logout(request)  # Log the user out
    return redirect('home')


def profile(request):
    if not request.session.get('user_id'):
        return redirect('login')  # Redirect to login if not authenticated

    # Get the current user based on the session user ID
    user = StudentModel.objects.get(id=request.session['user_id'])

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()  # Save the updated user profile
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = StudentProfileForm(instance=user)

    return render(request, 'profile.html', {'form': form, 'user': user})