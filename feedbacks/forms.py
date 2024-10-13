from django import forms
from django.contrib.auth.hashers import make_password
from .models import ProblemsModel, OffersModel, StudentModel


class StudentRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    full_name = forms.CharField(disabled=True, required=False)  # Use disabled=True instead of readonly

    class Meta:
        model = StudentModel
        fields = ['full_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['full_name'].initial = self.instance.full_name

    # Validate that the two passwords match
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    # Save the user with the hashed password
    def save(self, commit=True):
        student = super().save(commit=False)
        student.password = make_password(self.cleaned_data['password1'])  # Hash the password
        if commit:
            student.save()
        return student

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['username', 'first_name', 'last_name', 'organization_name', 'location', 'email', 'linkedin_profile', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'organization_name': forms.TextInput(attrs={'placeholder': 'Enter your organization name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter your location'}),
            'email': forms.EmailInput(attrs={'readonly': 'readonly', 'style': 'cursor: not-allowed;', 'placeholder': 'Enter your email address'}),
            'linkedin_profile': forms.URLInput(attrs={'placeholder': 'Enter your LinkedIn profile link'}),
            'profile_picture': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

class ProblemForm(forms.ModelForm):
    class Meta:
        model = ProblemsModel
        fields = ['title', 'description']

class OfferForm(forms.ModelForm):
    class Meta:
        model = OffersModel
        fields = ['title', 'description']